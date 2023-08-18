# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Constraints:

#     nums1.length == m + n
#     nums2.length == n
#     0 <= m, n <= 200
#     1 <= m + n <= 200
#     -109 <= nums1[i], nums2[j] <= 109


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i1, i2 = m-1, n-1
        for i in range(len(nums1)-1, -1, -1):
            if i2 == -1:
                break
            elif i1 == -1 or nums1[i1] <= nums2[i2]:
                nums1[i] = nums2[i2]
                i2 -= 1
            else:
                nums1[i] = nums1[i1]
                i1 -= 1
    
    def merge2(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i1, i2 = m-1, n-1
        for i in reversed(range(0, n+m)):
            if i2 == -1: break
            elif i1 == -1 or nums1[i1] <= nums2[i2]:
                nums1[i] = nums2[i2]
                i2 -= 1
            else:
                nums1[i] = nums1[i1]
                i1 -= 1
        
            
