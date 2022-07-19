# type: ignore
from functools import wraps

def log_it(prefix: str, suffix: str):
    def deco(func):
        @wraps(func)
        def updated_func(*args, **kargs):
            print(prefix)
            res = func(*args, **kargs)
            print(suffix)
            return res
        return updated_func
    return deco

@log_it(prefix='pre', suffix='after')
def prog(a: int, b: int) -> int:
    c = a + b
    print(f'a + b = {c}')
    return c

prog(1, 2)