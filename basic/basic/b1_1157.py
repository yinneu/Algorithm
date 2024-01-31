text = input().upper()
cnt = {}
lst = list(set(text))
print(lst)

for t in text:
    if t in cnt:
        cnt[t] += 1
    else:
        cnt[t] = 1

sort_cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
maxN = sort_cnt[0][0]
if len(sort_cnt) > 1:
    if sort_cnt[0][1] == sort_cnt[1][1]:
        maxN = '?'

print(maxN)

# list -> set으로 만들면 중복을 제거함.
# 해당 리스트로 count를 하여 별도의 리스트를 생성
# 리스트 2개로 가능함. 리스트가 활용도가 높으므로 리스트로 변환하여 하는게 좋은듯