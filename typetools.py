from functools import wraps
from inspect import signature

def checked(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sig = signature(func)
        bound = sig.bind(*args, **kwargs)
        ann = func.__annotations__
        for p, a in bound.arguments.items():
            if p in ann:
                assert isinstance(a, ann[p]), f'Type mismatch: Expected {ann[p]}, Got {type(a)}'
        return func(*args, **kwargs)
    return wrapper
