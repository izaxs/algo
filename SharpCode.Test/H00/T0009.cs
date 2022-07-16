namespace SharpCode;

public class T0009
{
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