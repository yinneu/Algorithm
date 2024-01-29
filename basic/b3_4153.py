import sys
input = sys.stdin.readline

while True:
    
    nums = list(map(int, input().split()))    
    if nums.count(0) == 3:
        break
    
    sortN = sorted(nums)    
    if pow(sortN[0], 2) + pow(sortN[1], 2) == pow(sortN[2], 2):
        print("right")
    else:
        print("wrong")