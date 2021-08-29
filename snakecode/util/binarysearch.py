def bisect_right(nums: list[int], target: int, lo: int = 0, hi: int = -1) -> int:
    if hi == -1: hi = len(nums)
    if lo < 0: lo = 0
    while lo < hi:
        mid = (lo+hi) >> 1
        if target < nums[mid]: hi = mid
        else: lo = mid+1
    return lo

def bisect_left(nums: list[int], target: int, lo: int = 0, hi: int = -1) -> int:
    if hi == -1: hi = len(nums)
    if lo < 0: lo = 0
    while lo < hi:
        mid = (lo+hi) >> 1
        if nums[mid] < target: lo = mid+1
        else: hi = mid
    return lo

def bisect_any(nums: list[int], target: int, lo: int = 0, hi: int = -1) -> int:
    if hi == -1: hi = len(nums)
    if lo < 0: lo = 0
    while lo < hi:
        mid: int = (lo + hi) >> 1
        if nums[mid] < target: lo = mid + 1
        elif nums[mid] > target: hi = mid
        else:
            return lo
    return lo

def bisect_prox(nums: list[int], target: int, lo: int = 0, hi: int = -1) -> tuple[int, int]:
    if hi == -1: hi = len(nums)
    if lo < 0: lo = 0
    while lo < hi:
        mid: int = (lo + hi) >> 1
        if nums[mid] < target: lo = mid + 1
        elif nums[mid] > target: hi = mid
        else:
            return lo, hi
    return -1, -1

def bisect_range(nums: list[int], target: int) -> tuple[int, int]:
    lo, hi = bisect_prox(nums, target)
    lower = bisect_left(nums, target, lo, hi)
    higher = bisect_right(nums, target, lo, hi)
    return lower, higher

nums = [0, 1, 1, 2, 3, 3, 3, 4]
print(bisect_range(nums, 5))