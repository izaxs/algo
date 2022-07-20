namespace SharpCode;

public class S0003 
{
    public int LengthOfLongestSubstring(string s) 
    {
        int max = 0;
        int lo = -1;
        var lastSeen = new Dictionary<char, int>();
        for (int i = 0; i < s.Length; i++) {
            if (lastSeen.ContainsKey(s[i])) 
            {
                int lastIndex = lastSeen[s[i]];
                lo = Math.Max(lastIndex, lo);
            }
            lastSeen[s[i]] = i;
            max = Math.Max(max, i-lo);
        }
        return max;
    }

    public int LengthOfLongestSubstring2(string s) 
    {
        int max = 0, lo = -1;
        var lastSeen = new Dictionary<char, int>();
        for (int i = 0; i < s.Length; i++) 
        {
            lo = Math.Max(lo, lastSeen.GetValueOrDefault(s[i], -1));
            max = Math.Max(max, i-lo);
            lastSeen[s[i]] = i;
        }
        return max;
    }
}