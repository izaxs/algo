namespace SharpCode;

public class S0009
{
    public bool IsPalindrome(int x)
    {
        if (x == 0) return true;
        if (x < 0 || x%10 == 0) return false;
        int b = 0;
        for (; x > b; x /= 10) b = b*10 + x%10;
        return x == b || x == b / 10;
    }
}
