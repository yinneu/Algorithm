import sys
input = sys.stdin.readline

w, h = map(int, input().split())
print('%.1f' %((w*h)/2)) # % 서식문자