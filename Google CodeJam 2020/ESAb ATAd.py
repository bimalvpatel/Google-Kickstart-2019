import sys

def flip(result):
    return [str(int(x)^1) for x in result]

def reverse(result):
    return result[::-1]

def query(i,count):
    if i is not None:
        print(str(i+1))
    else:
        print('1')
    sys.stdout.flush()
    return input(),count+1

def esab_atad(B):
    result = [0]*B
    same,diff = None,None
    count = 0
    for i in range(B//2):
        if count and count%10 == 0:
            sameresponse,count = query(same,count)
            diffresponse,count = query(diff,count)
            if same is not None and int(sameresponse)^int(result[same]):
                result = flip(result)
            if diff is not None and int(diffresponse)^int(result[diff]):
                result = reverse(result)
        result[i],count = query(i,count)
        result[B-i-1],count = query(B-i-1,count)
        if result[i] == result[B-i-1]:
            same = i
        if result[i] != result[B-i-1]:
            diff = i
    print(''.join(result))
    sys.stdout.flush()
    verdict = input()
    if verdict != 'Y':
        exit()

if __name__ == '__main__':
    T,B = map(int,input().split())
    for i in range(T):
        esab_atad(B)





