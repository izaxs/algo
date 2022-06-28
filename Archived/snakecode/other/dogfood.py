def feedDog(sp: list[str], k: int) -> int:
    feedCount = 0
    nextDog = 0
    for i, v in enumerate(sp):
        if v != 'F': continue
        while nextDog < min(i+k+1, len(sp)):
            if sp[nextDog] != 'D':
                nextDog += 1
                continue
            if abs(nextDog-i) <= k: break
            nextDog += 1
        if nextDog == len(sp): return feedCount
        if sp[nextDog] == 'D' and abs(nextDog-i) <= k:
            feedCount += 1
            nextDog += 1
    return feedCount

def test():
    sp = ['D', 'D', 'F', 'F', 'D']
    sp = ['D', 'D', 'F', 'F', 'D', 'D', 'D', 'F', 'F', 'D', 'D']
    # sp = ['D', 'D', 'D', 'F', 'F', 'F']
    # sp = ['D', 'D', 'D', 'D', 'D', 'D']
    # sp = ['F', 'F', 'F', 'D', 'F', 'F']
    print(feedDog(sp, 1))

test()