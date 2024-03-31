# 공백이 있는 문자를 출력 해야하는 경우 strip()을 주의해야한다. " adb" -> "abd" 가 됨
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(1, n+1):
    stm = input().strip('\n')
    print(f'%d. %s' %(i, stm))