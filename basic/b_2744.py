text = input()

for t in text:
    if t.isupper():
        print(t.lower(), end="")
    else:
        print(t.upper(), end="")
        
# 대소문자 상호변환 swapcase()