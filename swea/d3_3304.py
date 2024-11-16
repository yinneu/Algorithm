#LCS: 최장 공통 부분 수열, 최장 공통 부분 문자열은 같은 경우만 보면됨.
T = int(input())

for t in range(1, T+1):
    s1, s2 = input().split()

    lt = [[0 for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]
    for i in range(1, len(s2)+1):
        for j in range(1, len(s1)+1):
            if s2[i-1] == s1[j-1]:
                lt[i][j] = lt[i-1][j-1] + 1
            else:
                lt[i][j] = max(lt[i][j-1], lt[i-1][j])

    print(f'#{t} {max(lt[len(s2)])}')