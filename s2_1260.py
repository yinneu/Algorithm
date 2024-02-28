import sys
input = sys.stdin.readline

dic = {}
dicb = {}
dfsr = []
bfsr = []
def dfs(n):   
    dfsr.append(n)
    dic[n][0] = 0   
    dic[n].sort()
    for i in range(1, len(dic[n])):
        if dic[i][0] == -1:    #아직 탐색하지 않은 경우
            dfs(dic[n][i])
        
# def bfs(n): 보류
#     dicb[n][0] = 0
#     dic[n].sort()
#     for i in range(1, len(dic[n])):
#         if dicb[i][0] == -1:
#             bfsr.append(i)        
            
#     for i in range(1, len(dic[n])):
#         if dic[i][0] == -1:
#             bfs(dic[i])


n, m, v = map(int,input().split())       
for _ in range(m):
    a, b = map(int, input().split())
    
    if a in dic:
        dic[a].append(b)
    else:
        dic[a] = [-1, b]  
        dicb[a] = [-1]  
    if b in dic:
        dic[b].append(a)
    else:
        dic[b] = [-1, a]
        dicb[b] = [-1]
    
print(dic)
dfs(v)
print(dfsr)
bfs(v)
print(bfsr)
        