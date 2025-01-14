import sys

nums = []
maxV = 0
maxI = 0

for i in range(9):
    nums.append(int(sys.stdin.readline()))

for i in range(9):
    if (nums[i] > maxV):
        maxV = nums[i]
        maxI = i+1

print(maxV)
print(maxI)

# max, list.index 쓰면 편함 ^^