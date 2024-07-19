# 지능형 기차
# 총 4개의 역을 지나면서 기차 안에 가장 많은 사람이 가장 많을 때, 그 사람 수를 구하라.

max = 0
person = 0

for i in range(4):
    out,inn = map(int, input().split())
    person = person - out + inn
    if person > max:
        max = person
    
print(max)