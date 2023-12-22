from functools import wraps


def inject_objects(**objects):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for k, v in objects.items():
                func.__globals__[k] = v
            res = func(*args, **kwargs)
            for k, v in objects.items():
                del func.__globals__[k]
            return res

        return wrapper

    return decorator
