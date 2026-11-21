# Performance Benchmark Demo

This folder is for a Codex project that refactors the following 
pure-Python dice-roll snippet into a small benchmark that compares
the pure-Python implementation using `random.randrange` with 
Codex-generated Python code that performs significantly faster for
large numbers of die rolls.

Pure-Python dice-roll snippet:

```python
import random
rolls_list = [random.randrange(1, 7) for i in range(0, 600_000_000)]
```

