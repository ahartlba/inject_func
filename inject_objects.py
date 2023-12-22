from functools import wraps

class inject_objects:
    def __init__(self, cleanup: bool = True, **objects):
        self._cleanup = cleanup
        self._objects = objects

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for k, v in self._objects.items():
                func.__globals__[k] = v
            res = func(*args, **kwargs)
            if self._cleanup:
                for k, v in self._objects.items():
                    del func.__globals__[k]
            return res
        return wrapper
