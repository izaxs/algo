def parse_ip(inputStr: str, n: int) -> list[str]:
    results: list[str] = []
    helper(inputStr, 0, 0,'', n, results)
    return results

def helper(inputStr: str, curIndex: int, curVal: int, ip: str, n: int, ret: list[str]):
    if curIndex == len(inputStr):
        if n == 0:
            ret.append(ip)
        return
    if n == 0:
        return
    curVal = curVal * 10 + int(inputStr[curIndex])
    if curVal < 26 and curVal > 0:
        helper(inputStr, curIndex + 1, curVal, ip, n, ret)
    if curVal <= 255:
        ip = str(curVal) if not ip else ip + '.' + str(curVal)
        helper(inputStr, curIndex + 1, 0, ip, n - 1, ret)

IPs = parse_ip("2402411", 5)
print(IPs)

IPs2 = parse_ip("500012", 5)
print(IPs2)
