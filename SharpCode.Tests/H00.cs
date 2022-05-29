namespace SharpCode.Tests;

public class H00
{
    [Fact]
    public void TestS0001() {
        var sln = new S0001();
        var res = sln.TwoSum(new int[] { 2, 4, 1, 9, 7, 3 }, 8);
        Assert.Equal(new int[] { 2, 4 }, res);
    }
}