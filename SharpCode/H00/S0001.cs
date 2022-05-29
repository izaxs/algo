namespace SharpCode;

public class S0001 {
    public int[] TwoSum(int[] nums, int target) {
        var expect = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++) {
            if (expect.TryGetValue(nums[i], out int last)) {
                return new int[2] { last, i };
            }
            expect[target - nums[i]] = i;
        }
        return new int[2];
    }
}
