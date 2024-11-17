T = int(input())

for t in range(1, T+1):
    N = int(input())

    nums = set()
    cnt = 1
    while True:
         n = N * cnt
         ss = str(n)

         for i in ss:
             if i not in nums:
                 nums.add(i)

         if len(nums) == 10:
             break

         cnt += 1

    print(f'#{t} {N*cnt}')