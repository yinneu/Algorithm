import sys
input = sys.stdin

n = int(input.readline())
nums = list(map(int, input.readline().split()))
v = int(input.readline())
cnt = 0

for num in nums:
    if num == v:
        cnt += 1
        
print(cnt)

# list.count(k) => 해당 요소의 개수가 나옴
# 여러 요소가 아닌 하나의 요소는 굳이 sys.stdin을 안써도 될 듯 함.