'''

Round A 3
https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3f5b

'''

import math
import collections
def ispossible(midvalue,distances,additional):
    for distance in sorted(distances,reverse=True):
        if distance <= midvalue:
            break
        additional -= (math.ceil(distance/midvalue)-1)*distances[distance]
        if additional < 0:
            break
    return additional >= 0

def solve():
    noofsessions, additional = map(int,input().split())
    times = list(map(int,input().split()))
    left = 1
    right = 1
    distances = collections.defaultdict(int)
    for i in range(1,len(times)):
        distances[times[i]-times[i-1]] += 1
        right = max(right,times[i]-times[i-1])
    while left <= right:
        mid = left + (right-left)//2
        if ispossible(mid,distances,additional):
            right = mid - 1
        else:
            left = mid + 1
    return left



if  __name__ == '__main__':
    for i in range(int(input())):
        print("Case #"+str(i+1)+": "+str(solve()))