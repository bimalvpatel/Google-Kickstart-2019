import collections
def check(mid,minc,maxc,minr,maxr,pos):
    locr = []
    locc = []
    if (maxr-minr)%2==0:
        locr = [minr+(maxr-minr)//2]
    else:
        locr = [minr+(maxr-minr)//2,minr+(maxr-minr)//2+1]
    if (maxc-minc) % 2==0:
        locc = [minc+(maxc-minc)//2]
    else:
        locc = [minc+(maxc-minc)//2,minc+(maxc-minc)//2+1]
    return min(max(abs(mr - r) + abs(mc - c) for r, c in pos) for mr in locr for mc in locc) <= mid

def solve():
    R,C = [int(i) for i in input().split()]
    d = []
    for i in range(R):
        d.append(input())
    delivery = [[float("inf")]*C for _ in range(R)]
    deliverytimemap = collections.defaultdict(list)
    ans = 0
    queue = collections.deque()
    for i in range(R):
        for j in range(C):
            if d[i][j] == '1':
                queue.append((i,j))
                delivery[i][j] = 0
    if not queue:
        return R//2 + C//2
    while queue:
        i,j = queue.popleft()
        val = delivery[i][j]
        for x,y in ((-1,0),(0,-1),(1,0),(0,1)):
            if 0 <= i+x<R and 0<=j+y<C and delivery[i+x][j+y] > val+1:
                deliverytimemap[val+1].append((i+x,j+y))
                delivery[i+x][j+y] = val+1
                queue.append((i+x,j+y))
                ans = max(ans,val+1)
    if ans == 0:
        return ans
    low = 0
    high = ans
    while low < high:
        mid  =  (low+high)//2
        pos =  []
        minc = float('inf')
        maxc = -1
        minr = float('inf')
        maxr = -1
        for key in deliverytimemap:
            if key > mid:
                for arr in deliverytimemap[key]:
                    pos.append(arr)
                    minc = min(minc,arr[1])
                    maxc = max(maxc,arr[1])
                    minr = min(minr,arr[0])
                    maxr = max(maxr,arr[0])
        if check(mid,minc,maxc,minr,maxr,pos):
            high = mid
        else:
            low  =  mid+1
    return low
if __name__ == '__main__':
    for i in range(int(input())):
        print("Case #{}: {}".format(i+1,solve()))