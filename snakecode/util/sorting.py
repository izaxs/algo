from typing import Callable
import time
import random

def bubbleSort(nums: list[int]):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                swapped = True

def selectionSort(nums: list[int]):
    for i in range(len(nums)-1):
        smallestIndex = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[smallestIndex]:
                smallestIndex = j
        nums[i], nums[smallestIndex] = nums[smallestIndex], nums[i]

def insertionSort(nums: list[int]):
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j-1] < nums[j]:
                break
            nums[j-1], nums[j] = nums[j], nums[j-1]

def quickSort(nums: list[int], lo: int = 0, hi: int = -1):
    def partition(nums: list[int], lo: int, hi: int) -> int:
        # return pivot index, left[] < pivot <= right[]
        lower = lo
        for i in range(lo, hi):
            if nums[i] < nums[hi]:
                nums[lower], nums[i] = nums[i], nums[lower]
                lower += 1
        nums[lower], nums[hi] = nums[hi], nums[lower]
        return lower
    if hi == -1: hi = len(nums)-1
    if lo >= hi: return
    pivot = partition(nums, lo, hi)
    quickSort(nums, lo, pivot-1)
    quickSort(nums, pivot+1, hi)

def mergeSort(nums: list[int]):
    pass

class SortingTemplate:
    def sort(self, nums: list[int]) -> list[int]:
        if not nums: return []
        self._quickSort(nums, 0, len(nums)-1)
        return nums

    def _quickSort(self, nums: list[int], lo: int, hi: int):
        if lo >= hi: return
        pivot = self._partition(nums, lo, hi)
        self._quickSort(nums, lo, pivot-1)
        self._quickSort(nums, pivot+1, hi)

    def _partition(self, nums: list[int], lo: int, hi: int) -> int:
        pivot = nums[lo]
        while lo < hi:
            while lo < hi and pivot <= nums[hi]:
                hi -= 1
            nums[lo] = nums[hi]
            while lo < hi and nums[lo] <= pivot:
                lo += 1
            nums[hi] = nums[lo]
            nums[lo], nums[hi] = nums[hi], nums[lo]
        nums[lo] = pivot
        return lo

def quickSortWrapper1(nums: list[int]) -> list[int]:
    _ = SortingTemplate()
    quickSort(nums, 0, len(nums)-1)
    return nums

def quickSortWrapper2(nums: list[int]) -> list[int]:
    s = SortingTemplate()
    s.sort(nums)
    return nums

def measure_execution(func: Callable[[list[int]], list[int]], cases: list[list[int]], msg: str):
    tik = time.perf_counter()
    for case in cases:
        func(case)
    tok = time.perf_counter()
    print(f'{msg}: function elapsed in {tok-tik}')

def gen_cases(lo: int, hi: int, listLen: int, casesLen: int) -> list[list[int]]:
    res: list[list[int]] = []
    for _ in range(casesLen):
        res.append(random.sample(range(lo, hi), listLen))
    return res

def casesAreSorted(cases: list[list[int]]) -> bool:
    for nums in cases:
        minNum = float('-inf')
        for n in nums:
            if n < minNum: return False
            minNum = n
    return True

def benchMark():
    # caseSet1 = gen_cases(lo=0, hi=1000, listLen=200, casesLen=500)
    caseSet2 = gen_cases(lo=0, hi=100_000_000, listLen=1_000_000, casesLen=1)
    # measure_execution(quickSortWrapper1, caseSet1, 'cases1')
    measure_execution(quickSortWrapper2, caseSet2, 'cases2')
    # assert(casesAreSorted(caseSet1))
    assert(casesAreSorted(caseSet2))

if __name__ == '__main__':
    inputs = [4, 13, 8, 10, 6, 0, 7, 5, 9, 4, 1, 14, 8, 2]

    # bubbleSortCase = unsorted[:]
    # bubbleSort(bubbleSortCase)
    # print(bubbleSortCase)

    # selectionSortCase = unsorted[:]
    # selectionSort(selectionSortCase)
    # print(selectionSortCase)

    # insertionSortCase = unsorted[:]
    # insertionSort(insertionSortCase)
    # print(insertionSortCase)

    # quickSortCase = unsorted[:]
    # quickSort(quickSortCase)
    # print(quickSortCase)
    # s = SortingTemplate()
    # s.sort(inputs)
    # print(inputs)

    benchMark()
