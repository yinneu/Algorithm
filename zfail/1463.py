import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def cal(n):
    
    if n == 2 or n == 3:
        return 1   
        
    m2 = n % 2
    m3 = n % 3
            
    return min(cal(n//3)+1+m3, cal(n//2)+1+m2)

n = int(input())
print(cal(n))
