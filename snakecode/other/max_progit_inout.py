def maxProfit(prices: list[int]) -> int:
    minInt = -(1 << 32)
    s = [[minInt]*5, [minInt]*5]
    for i in prices:
        s[1][1] = max(i, s[0][1]+i)
        s[1][2] = max(i, s[0][1]+i, s[0][2])
        s[1][3] = max(i, s[0][2]+i, s[0][3]+i)
        s[1][4] = max(i, s[0][3]+i, s[0][4])
        s.reverse()
    return s[0][4]

print(maxProfit([-2, 6, -4, 3, 2]))
print(maxProfit([-2, -6, -4, -3, -2]))