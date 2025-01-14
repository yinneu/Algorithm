n = int(input())
nums = list(map(int, input().split()))

#1 368ms
print(min(nums))
print(max(nums))

#2 672ms
# sorted_nums = sorted(nums)
# print(sorted_nums[0])
# print(sorted_nums[-1])


# 틀림ㅎ
# for i in range(1, n-1):
#     if nums[0] < nums[i]:
#         nums[0], nums[i] = nums[i] ,nums[0] # swap

# for i in range(n-2, -1, -1):
#     if nums[-1] > nums[i]:
#         nums[-1], nums[i] = nums[i] ,nums[-1] # swap
        
# print(nums[-1], nums[0])