package h01

class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val map = mutableMapOf<Int, Int>()
        for ((i, v) in nums.withIndex()) {
            map[v]?.let { return intArrayOf(it, i)}
            map[target-v] = i
        }
        return intArrayOf()
    }
}