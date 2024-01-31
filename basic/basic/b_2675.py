n = int(input())

for _ in range(n):
    cnt, text = input().split()
    cnt = int(cnt)
    for t in text:
        print(t * cnt , end="")
    print()