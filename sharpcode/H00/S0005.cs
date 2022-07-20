namespace SharpCode;

class S0005 {
    private int maxLo = 0;
    private int maxHi = 0;
    public string LongestPalindrome(string s) 
    {
        int offset = 0, offsetLimit = 0;
        int mid = offsetLimit = s.Length/2;
        while (offset <= offsetLimit)
        {
            Update(s, mid-offset, mid-offset);
            Update(s, mid-offset-1, mid-offset);
            Update(s, mid+offset, mid+offset);
            Update(s, mid+offset-1, mid+offset);
            offset++;
        }
        return s.Substring(maxLo, maxHi-maxLo+1);
    }

    private void Update(string s, int loMid, int hiMid) 
    {
        while (loMid >= 0 && hiMid < s.Length && s[loMid] == s[hiMid])
        {
            loMid--;
            hiMid++;
        }
        if (hiMid-loMid-1 > maxHi-maxLo+1)
        {
            maxHi = hiMid-1;
            maxLo = loMid+1;
        }
    }
}