# https://www.acmicpc.net/problem/5597
import sys

std = [ i for i in range(1, 31)]
onstd = []

for _ in range(28):
    onstd.append(int(sys.stdin.readline().strip()))
    
result = sorted(list(set(std) - set(onstd)))

for i in result:
    print(i)
    
# sys.stdin.readline() : 개행문자 제거 안됨.
# list.sort() : 반환 안됨. 제자리 정렬 , sorted(list) : 반환됨.
# list(range()) -> 해당 값 리스트 생성