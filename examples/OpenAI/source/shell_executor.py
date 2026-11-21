"""ReadOnlyShellExecutor — a safe, allowlist-based ShellTool executor.

Used by 02-05-08-shell-tool-readme-generator.ipynb.
Import with:
    from source.shell_executor import ReadOnlyShellExecutor
"""

import asyncio
import os
from pathlib import Path

from agents import (
    ShellCallOutcome,    # stores whether a command exited normally or timed out
    ShellCommandOutput,  # stores one command's stdout, stderr, and outcome
    ShellCommandRequest, # passed to the executor; contains the commands to run
    ShellResult,         # wraps a list of ShellCommandOutputs; returned to the SDK
)


class ReadOnlyShellExecutor:
    """ShellTool executor that allows only a safe list of read-only commands.

    ShellTool does not run commands itself — it delegates execution to this
    callable. By defining our own executor we can apply an allowlist before
    anything reaches the OS, giving the agent access to file-inspection
    commands while blocking writes, network calls, and shell injection.

    Two layers of protection:
    1. `allowed_prefixes`  — only commands that start with these strings pass
    2. `blocked_fragments` — presence of any of these in the command is an
       immediate rejection (prevents piping, chaining, and sub-shells)
    """

    # Commands the agent is permitted to run, matched against the start of
    # the command string (after stripping leading whitespace).
    allowed_prefixes: tuple[str, ...] = (
        'pwd',
        'ls ',
        'find ',
        'sed -n ',
        'head ',
        'cat ',
        # Windows equivalents
        'dir ',
        'type ',
    )

    # Strings that indicate a dangerous command regardless of the prefix.
    # These block shell injection, piping, chaining, and mutating commands.
    blocked_fragments: tuple[str, ...] = (
        '>', '>>', '|', ';', '&&', '||', '`', '$(',  '\n',
        ' rm ', ' mv ', ' cp ', ' touch ', ' mkdir ', ' chmod ',
        ' chown ', ' curl ', ' wget ', ' python ', ' python3 ',
    )

    def __init__(self, working_folder: Path | None = None):
        # All relative paths in shell commands are resolved against this folder.
        # Defaults to the current working directory so notebooks work without
        # extra configuration.
        self.working_folder = Path(working_folder or Path.cwd())

    def is_allowed(self, command: str) -> bool:
        """Return True only for simple, safe read-only inspection commands.

        Checks both the allowlist and the blocklist. The blocklist takes
        precedence — a command that starts with an allowed prefix but contains
        a blocked fragment (e.g. 'ls . | rm -rf /') is still rejected.
        """
        # Pad with spaces so fragment checks like ' rm ' match whole words
        # and do not fire on filenames that happen to contain those letters.
        normalized = f' {command.strip()} '

        if any(fragment in normalized for fragment in self.blocked_fragments):
            return False

        stripped = command.strip()
        # 'pwd' has no arguments, so check equality separately; all other
        # allowed commands are matched by prefix (they require a path/arg).
        return stripped == 'pwd' or stripped.startswith(self.allowed_prefixes)

    async def __call__(self, request: ShellCommandRequest) -> ShellResult:
        """Execute approved commands; return a blocked-command error for others.

        The SDK calls this method after ShellTool decides to run a shell
        command. For each command in the request we either run it in a
        subprocess or return a synthetic error, then wrap all results in a
        ShellResult for the SDK to forward to the model.
        """
        action = request.data.action
        command_outputs: list[ShellCommandOutput] = []

        for command in action.commands:
            if not self.is_allowed(command):
                # Return a synthetic error rather than running the command.
                # Exit code 126 means "command not executable" by POSIX convention.
                command_outputs.append(ShellCommandOutput(
                    command=command,
                    stdout='',
                    stderr='Blocked by ReadOnlyShellExecutor.',
                    outcome=ShellCallOutcome(type='exit', exit_code=126),
                ))
                continue

            # Run the command as a subprocess, capturing stdout and stderr.
            # `env=os.environ.copy()` ensures PATH and other variables are
            # inherited so commands like `find` resolve correctly.
            process = await asyncio.create_subprocess_shell(
                command,
                cwd=self.working_folder,
                env=os.environ.copy(),
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )

            try:
                # Enforce a 10-second timeout so a slow command cannot stall
                # the agent run indefinitely.
                stdout, stderr = await asyncio.wait_for(
                    process.communicate(), timeout=10
                )
                outcome = ShellCallOutcome(type='exit', exit_code=process.returncode)
            except asyncio.TimeoutError:
                process.kill()
                stdout, stderr = await process.communicate()
                # 'timeout' tells the model the command was killed, not that
                # it completed — the model can retry with a narrower scope.
                outcome = ShellCallOutcome(type='timeout', exit_code=None)

            command_outputs.append(ShellCommandOutput(
                command=command,
                stdout=stdout.decode('utf-8', errors='replace'),
                stderr=stderr.decode('utf-8', errors='replace'),
                outcome=outcome,
            ))

        return ShellResult(
            output=command_outputs,
            provider_data={'working_folder': str(self.working_folder)},
        )
