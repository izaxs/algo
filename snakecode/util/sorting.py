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
    

if __name__ == '__main__':
    unsorted = [4, 13, 8, 10, 6, 0, 7, 5, 9, 4, 1, 14, 8, 2]
    # bubbleSortCase = unsorted[:]
    # bubbleSort(bubbleSortCase)
    # print(bubbleSortCase)

    # selectionSortCase = unsorted[:]
    # selectionSort(selectionSortCase)
    # print(selectionSortCase)

    # insertionSortCase = unsorted[:]
    # insertionSort(insertionSortCase)
    # print(insertionSortCase)

    quickSortCase = unsorted[:]
    quickSort(quickSortCase)
    print(quickSortCase)
