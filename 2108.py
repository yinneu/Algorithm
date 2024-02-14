# 산술평균 : N개의 수들의 합을 N으로 나눈 값 -> 첫째 자리에서 반올림
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값  여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
import sys
input = sys.stdin.readline

arr = []
trr = []
n = int(input())

for _ in range(n):
    arr.append(int(input()))
    
arr.sort()
srr = list(set(arr))

for i in srr:
    trr.append([i,arr.count(i)])

trr.sort(key = lambda x : (-x[1], x[0]))

print(round(sum(arr)/n)) #평균
print(arr[n//2])  #중앙값
if len(trr) > 1:
    if trr[0][1] == trr[1][1]:
        print(trr[1][0])
    else:
        print(trr[0][0])
else:
    print(trr[0][0])
print(arr[-1]-arr[0]) #범위



