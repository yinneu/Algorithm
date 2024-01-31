import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort(reverse = True)
print(nums)
maxN = 0
for i in range(0, n-2):
    Sum = nums[i] + nums[i+1] + nums[i+2]
    
    if Sum <= m and Sum > maxN:
        maxN = Sum
print(maxN)


## 조합찾기?