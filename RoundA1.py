def solve():
    N, P = [int(i) for i in input().split()]
    skill = [int(i) for i in input().split()]
    d = {}
    for s in skill:
        if s not in d:
            d[s] = 0
        d[s] += 1
    # print(d)
    total = {}
    if max(d.values()) >= P:
        return 0
    for key in d:
        total[key] = P * key
    skill = []
    for key in sorted(d.keys()):
        i = 0
        while i < d[key]:
            skill.append(key)
            i += 1
    s = [sum(skill[:P])]
    j = P
    while j < N:
        s.append(s[-1] - skill[j - P] + skill[j])
        j += 1
    ans = float("inf")
    for i in range(P - 1, N, 1):
        ans = min(ans, total[skill[i]] - s[i - P + 1])
    return ans


if __name__ == '__main__':
    for i in range(int(input())):
        print("Case #{}: {}".format(i + 1, solve()))