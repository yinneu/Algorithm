# 산술평균 : N개의 수들의 합을 N으로 나눈 값 -> 첫째 자리에서 반올림
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값  여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
import sys
input = sys.stdin.readline

def many(dic):
    
    lt = []
    maxN = max(list(dic.values())) #최댓값
    keys = list(dic.keys())
    
    for k in keys:
        if dic[k] == maxN:
            lt.append(k)
            
    lt.sort()
    if len(lt) > 1:
        return lt[1]
    
    return lt[0]

dic = {}
lt = []
n = int(input())
for _ in range(n):
    a = int(input())
    lt.append(a)
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1

lt2 = sorted(lt)
 
print(round(sum(lt2) / n)) # 평균

print(lt2[n//2])  #중앙값

print(many(dic)) # 최빈값

print(abs(lt2[-1]-lt2[0])) #범위



# 참고: 처음에 생각했던 것처럼 데이터 범위가 작으므로 인덱스를 활용하는게 좋음.
# 중앙값, 최대, 최소를 체크하는 방식이 좋음. ㅇㅇ,,
# 위에 풀이는 메모리, 시간 모두 많이 소요됨.
# import sys
# input = sys.stdin.readline

# N = int(input())
# nums = [0]*8001

# for _ in range(N):
#     n = int(input())
#     nums[n+4000] += 1

# Sum=0
# max_count=max(nums)
# temp=0
# min=4000
# max=-4000
# mid=0
# for i in range(-4000,4001):
#     count = nums[i+4000]
#     num = i
#     if count==0:
#         continue
#     else:
#         Sum += num*count
#         if count == max_count and temp<2:
#             mode = num
#             temp += 1
#         if num >= max:
#             max = num
#         if num <= min:
#             min = num
#         if mid <= N//2:
#             mid += count
#             if mid > N//2:
#                 center = num

# print(round(Sum/N))
# print(center)
# print(mode)
# print(max-min)
