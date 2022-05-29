package h00

import org.junit.jupiter.api.Assertions.assertArrayEquals
import org.junit.jupiter.api.Test

internal class Solution0001Test {
    private val sln = Solution()

    @Test
    fun twoSum() {
        val nums = intArrayOf(2, 4, 1, 9, 7, 3)
        val res = sln.twoSum(nums, 8)
        assertArrayEquals(intArrayOf(2, 4), res)
    }
}