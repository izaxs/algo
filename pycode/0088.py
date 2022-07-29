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
