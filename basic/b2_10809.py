aph = list('abcdefghijklmnopqrstuvwxyz')
cnt = [-1 for _ in range(26)]
text = list(input())

for index, value in enumerate(text):
    t = aph.index(value)
    if cnt[t] == -1:
        cnt[t] = index
    
for i in cnt:
    print(i, end=" ")
    
# 문자열 그대로 써도 상관 ㄴㄴ
# list 만들 때 [-1] * n 이 편함 ㅇㅇ