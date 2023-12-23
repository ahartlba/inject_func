# Inject Objects

Inject objects into functions @ runtime.

Example:

```python
from inject_objects import inject_objects as inject

@inject(a=1, b=3)
def foo():
    return a + b

foo()  # returns 4
```
