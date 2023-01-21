# Input is a m x n matrix
def print2D(m: list[list[int]]) -> None:
    for r in m:
        print(r)

if __name__ == "__main__":
    image = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1],
    ]
    print2D(image)
