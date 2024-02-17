# 1. append for문
# 2. for 이중
# 랜선의 길이는 2^31-1보다 작거나 같은 자연수 => 시간초과가 날 수 밖에 없다,,
# 이중탐색을 사용해야 하는 문제
import sys
input = sys.stdin.readline

arr = []
k, n = map(int, input().split())
for _ in range(k):
    arr.append(int(input()))

start = 1
end = max(arr)
while start < end:
    mid = (start + end) // 2 
    if mid == start: # start와 end가 1차이만 나는 경우
        mid = end
        
    count = sum(a // mid for a in arr)
    
    if count >= n:
        start = mid
    else:
        end = mid - 1
        
else:
    print(end)