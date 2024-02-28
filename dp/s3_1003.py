import sys
input = sys.stdin.readline

arr = [(1,0), (0,1)] # 0, 1의 개수

for i in range(2,41):
    n = arr[i-1][0] + arr[i-2][0]
    m = arr[i-1][1] + arr[i-2][1]
    arr.append((n, m))
    
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        k = int(input())
        print(arr[k][0],arr[k][1])