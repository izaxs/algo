# 1570. Dot Product of Two Sparse Vectors

# Given two sparse vectors, compute their dot product.

# Implement class SparseVector:

#     SparseVector(nums) Initializes the object with the vector nums
#     dotProduct(vec) Compute the dot product between the instance of SparseVector and vec

# A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

# Follow up: What if only one of the vectors is sparse?

# Constraints:

#     n == nums1.length == nums2.length
#     1 <= n <= 10^5
#     0 <= nums1[i], nums2[i] <= 100
from __future__ import annotations


class SparseVector:
    def __init__(self, nums: list[int]):
        self.m = {i: v for i, v in enumerate(nums) if v}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: SparseVector) -> int:
        a, b = self.m, vec.m
        if len(b) < len(a): a, b = b, a
        product = 0
        for i, v in a.items(): 
            if not (bv := b.get(i)): continue
            product += v * bv
        return product
        

        


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)