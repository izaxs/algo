# Input: gains[i]: earn gains[i] at ith day, if logged in
# Output: maximum profit, log in at least once
# Yes, the state machine approach kills all

def maxProfitWithOneRound(gains: list[int]) -> int:
    minInt = -(1 << 32)
    s0, s1 = minInt, minInt
    for i in gains:
        s0 = max(i, s0+i)
        s1 = max(s0, s1)
    return s1

def maxProfitWithTwoRounds(gains: list[int]) -> int:
    minInt = -(1 << 32)
    s = [[minInt]*5, [minInt]*5]
    for i in gains:
        s[1][1] = max(i, s[0][1]+i)
        s[1][2] = max(s[1][1], s[0][2])
        s[1][3] = max(s[0][2]+i, s[0][3]+i)
        s[1][4] = max(s[1][3], s[0][4])
        s.reverse()
    return max(s[0][2], s[0][4])

def maxProfitWithTwoRounds_better(gains: list[int]) -> int:
    minInt = -(1 << 32)
    states: list[int] = [minInt]*5
    for i in gains:
        states[3] = max(states[2]+i, states[3]+i)
        states[4] = max(states[3], states[4])
        states[1] = max(i, states[1]+i)
        states[2] = max(states[1], states[2])
    return max(states[2], states[4])

def maxProfit(gains: list[int], rounds: int) -> int:
    minInt = -(1 << 32)
    statesCount = rounds*2
    states = [[minInt]*statesCount for _ in range(2)]
    for i in gains:
        for j in range(statesCount):
            if j == 0: # first time login
                states[1][j] = max(i, states[0][j]+i)
            elif j % 2 == 0: # login
                states[1][j] = max(states[0][j-1]+i, states[0][j]+i)
            else: # log out
                states[1][j] = max(states[1][j-1], states[0][j])
        # print(f'X Round: {i} -> {states[1]}')
        states.reverse()
    return max(states[0][1::2])

def maxProfit_best(gains: list[int], rounds: int) -> int:
    minInt, stateLen = -(1 << 32), rounds*2
    states = [minInt]*stateLen
    for i in gains:
        for j in range(stateLen-2, -1, -2):
            if j == 0: # first time login
                states[j] = max(i, states[j]+i)
            else:
                states[j] = max(states[j-1]+i, states[j]+i)
            states[j+1] = max(states[j], states[j+1])
    return max(states[1::2])


# print(maxProfitWithOneRound([-2, 6, -4, -3, -2]))
# print(maxProfitWithOneRound([-2, 7, -4, 3, 2, -5, 6]))

# print(maxProfitWithTwoRounds_better([-2, 6, -4, -3, -2]))
# print(maxProfitWithTwoRounds_better([-2, 7, -4, 3, 2, -5, 6]))

# print(maxProfit([-2, 6, -4, -3, -2], 1))
# print(maxProfit([-2, 7, -4, 3, 2, -5, 6], 1))
# print(maxProfit([-2, 6, -4, -3, -2], 2))
# print(maxProfit([-2, 7, -4, 3, 2, -5, 6], 2))

# print(maxProfit_best([-2, -10, -4, -1, -2], 1))
# print(maxProfit_best([-2, 6, -4, -3, -2], 1))

# p3 = [-2, 7, -4, 3, 2, -4, 6, -1, -2, 1, -3, 3, -2, -5, 10]

# rounds = 1
# print(maxProfitWithOneRound(p3))
# print(maxProfit(p3, rounds))
# print(maxProfit_best(p3, rounds))

# rounds = 2
# print(maxProfitWithTwoRounds_better(p3))
# print(maxProfit(p3, rounds))
# print(maxProfit_best(p3, rounds))

# rounds = 5
# print(maxProfit(p3, rounds))
# print(maxProfit_best(p3, rounds))
