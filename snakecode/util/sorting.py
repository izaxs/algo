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

def quickSort(nums: list[int]):
    pass

def mergeSort(nums: list[int]):
    pass

if __name__ == '__main__':
    unsorted = [4, 13, 8, 10, 6, 0, 7, 5, 9, 4, 1, 14, 8, 2]
    # bubbleSortCase = unsorted[:]
    # bubbleSort(bubbleSortCase)
    # print(bubbleSortCase)
    # selectionSortCase = unsorted[:]
    # selectionSort(selectionSortCase)
    # print(selectionSortCase)
    insertionSortCase = unsorted[:]
    insertionSort(insertionSortCase)
    print(insertionSortCase)
