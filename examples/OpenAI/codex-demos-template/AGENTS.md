# AGENTS.md

## Audience

These examples are for novice-to-intermediate-level programmers.

Favor clarity, directness, and predictable behavior over cleverness.

## Python style

- Target Python 3.14 unless otherwise specified.
- Generated code does not need to support earlier Python versions.   
- Use idiomatic Python with well-defined functions (and classes, if necessary)
- Use 4-space indents.
- Prefer single-quoted strings where appropriate.
- Use three double-quote characters to delimit docstrings and multiline strings.
- For scripts, include sample output in a docstring.
- Use type hints for new or substantially revised functions.
- Use concise, clear comments.
- Keep code lines to approximately 74-75 characters.

## Python environment

- Use conda environment `deitel-openai` for all Python scripts and tests.
- Run Python scripts with `conda run -n deitel-openai python <script>.py`.
- Run tests with `conda run -n deitel-openai python -m pytest -v`.
- Do not use plain `python`, `pip`, or `pytest` unless I explicitly ask.
- If a package is missing, report the exact `conda run` or `pip` command 
  needed to install it, but do not change environments unless asked.

## Java style

- Target Java 25 unless otherwise specified.
- Use 3-space indents.
- Use idiomatic Java with well-defined methods and classes.
- Use `printf` for formatted output.
- Put opening braces on the same line.
- Do not cuddle `else` in `if`/`else` and nested `if`/`else` statments.
- For full programs, include sample output in a multiline comment.

## Testing

- Prefer `pytest` for Python examples unless otherwise specified.
- Prefer JUnit for Java examples unless otherwise specified.
- Tests should verify behavior, not implementation details.
- For ambiguous behavior, ask clarification questions before writing tests.
- Run tests after creating or modifying them.

## Version control

- This workspace is one Git repository containing several independent demo folders.
- When working on a task, limit edits to the specified demo folder unless asked otherwise.
- Use `git status` and `git diff` to inspect changes.
- Do not create commits unless explicitly asked.
- When asked to commit, stage only files relevant to the current demo.
- Do not use `git add .` if unrelated files are modified.
- Do not push unless explicitly asked.
- Do not amend commits or rewrite Git history unless explicitly asked.
- Summarize changed files after each task.

## Git command ordering

- Do not run dependent Git commands in parallel.
- If a Git command changes repository state, wait for it to finish before
  running verification commands.
- Treat these as state-changing commands:
  - `git add`
  - `git commit`
  - `git mv`
  - `git rm`
  - branch or checkout operations
- After a state-changing Git command, run follow-up commands in sequence.
- Good sequence:
  1. `git add ...`
  2. `git diff --cached --stat`
  3. `git commit -m "..."`
  4. `git rev-parse --short HEAD`
  5. `git status --short`
- Do not run `git commit`, `git status`, and `git rev-parse` in the same
  parallel tool call.
- Only parallelize Git commands when they are independent and read-only.
- If a command depends on the result of a previous Git command, run it only
  after the previous command has completed.

This avoids race conditions where post-commit reads report stale repo state.

## Validation

- Run relevant scripts, tests, or compile commands when possible.
- Explain anything that could not be validated.
- Make the smallest high-confidence change that satisfies the request.
