'''

Plates
https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d40bb

'''

def solve():
    noofstacks, noofplates, neededplates = map(int, input().split())
    beautivalues = []

    for _ in range(noofstacks):
        beautivalues.append([0] + list(map(int, input().split())))

    for i in range(noofstacks):
        for j in range(1, noofplates + 1):
            beautivalues[i][j] += beautivalues[i][j - 1]

    dp = [[0] * (neededplates + 1) for _ in range(noofstacks)]
    for j in range(neededplates + 1):
        if j <= noofplates:
            dp[0][j] = beautivalues[0][j]
        else:
            dp[0][j] = beautivalues[0][-1]


    for i in range(1, noofstacks):
        for j in range(1, neededplates + 1):
            for k in range(min(j + 1, noofplates + 1)):
                dp[i][j] = max(dp[i][j], dp[i - 1][j - k] + beautivalues[i][k])


    return dp[-1][-1]


if __name__ == '__main__':
    for i in range(int(input())):
        print('Case #' + str(i + 1) + ": " + str(solve()))
