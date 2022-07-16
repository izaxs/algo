namespace SharpCode.Test;

/*
 * Tests for S0001 ~ S0099
 */
public class T00
{
    [Fact]
    public void TestS0001()
    {
        var sln = new S0001();
        var res = sln.TwoSum(new int[] { 2, 4, 1, 9, 7, 3 }, 8);
        Assert.Equal(new int[] { 2, 4 }, res);
    }

    [Fact]
    public void TestS0009()
    {
        var sln = new S0009();
        Assert.True(sln.IsPalindrome(121));
        Assert.False(sln.IsPalindrome(-121));
        Assert.False(sln.IsPalindrome(1210));
        Assert.True(sln.IsPalindrome(1221));
        Assert.False(sln.IsPalindrome(1321));
        Assert.True(sln.IsPalindrome(12321));
    }
}