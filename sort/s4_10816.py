# key : value (dictionary) 해시를 이용한 집합과 맵, 정렬
# 리스트.conut를 쓰면 시간초과
import sys
input = sys.stdin.readline

dic = {}

n = int(input())
arr = input().strip().split()

m = int(input())
marr = input().strip().split()

for a in arr:
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1
        
for b in marr:
    print(dic.get(b, 0), end=" ") # 해당 키가 있는지 검사 없으면 정해둔 디폴트값 리턴