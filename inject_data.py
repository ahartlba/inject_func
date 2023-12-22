from functools import wraps


def inject_data(func):
    @wraps(func)
    def wrapper(**kwargs):
        for k, v in kwargs.items():
            func.__globals__[k] = v
        res = func()
        for k, v in kwargs.items():
            del func.__globals__[k]
        return res

    return wrapper
