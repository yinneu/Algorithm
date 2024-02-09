import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    arr = []
    n, m = map(int, input().split())
    nums = input().strip().split()
    
    for i in range(0, len(nums)):
        arr.append([nums[i], i])
    
    nums.sort()
    cnt = 0 #출력 카운트
    
    while arr:
        npop = arr.pop(0)
        
        if npop[0] == nums[-1]:
            nums.pop()
            cnt += 1
            
            if npop[1] == m:
                print(cnt)
                break
        else:
            arr.append(npop)