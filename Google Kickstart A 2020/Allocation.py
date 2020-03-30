'''

Round A 1
https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3f56

'''

def solve():
    noofhouses, budget = map(int,input().split())
    houses = list(map(int,input().split()))
    houses.sort()
    i = 0
    while i < noofhouses and budget >= houses[i]:
        budget -= houses[i]
        i += 1
    return i



if __name__ == '__main__':
    for i in range(int(input())):
        print("Case #"+str(i+1)+": "+str(solve()))