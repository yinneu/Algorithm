import sys

text = []

while True:
    inputs = sys.stdin.readline().strip()
    
    if not text:
        text.append(inputs)
    else:
        if inputs == "":
            break
        text.append(inputs)

for t in text:
    print(t)
    
# 굳이 저장했다가 안해도 됨. 바로 입력 받아 출력해도 되는것,,