def numDecodings(s: str) -> int:
    pw, w, pd = 0, 1, ''
    for d in s:
        pw, w, pd = w, int(int(d) > 0) * w + int(9 < int(pd + d) < 27) * pw, d
    return w
