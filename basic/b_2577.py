nums = [int(input()) for _ in range(3)]
result = [0 for _ in range(10)]

mul_n = nums[0] * nums[1] * nums[2]
str_n = str(mul_n)

for i in str_n:
    result[int(i)] += 1
    
for r in result:
    print(r)
    
# 연산결과를 list로 만든 후, list.count(value)를 사용하면 된다.
# list(str_n).count(0~9)