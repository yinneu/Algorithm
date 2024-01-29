import sys

T = int(input())

for _ in range(T):
    score = 0
    inc = 1
    ox = sys.stdin.readline()
    
    for s in ox:
        if s == 'O':
            score += inc
            inc += 1
        else:
            inc = 1
    print(score)
            