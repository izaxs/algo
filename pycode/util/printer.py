import functools

# Input is a m x n matrix
def print2d(m: list[list[int]]) -> None:
    for r in m:
        print(r)

def monitor(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Entering {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Exiting {func.__name__} with {result=}")
        return result
    return wrapper


if __name__ == "__main__":
    image = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1],
    ]
    print2d(image)