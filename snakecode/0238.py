class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        products, it = [1] * len(nums), 1
        for i in range(len(nums) - 1, -1, -1):
            products[i] = it
            it *= nums[i]
        it = 1
        for i in range(len(products)):
            products[i] *= it
            it *= nums[i]
        return products
