import sys
input = sys.stdin.readline

def check(arr):
    chk = []

    for a in arr:
        if a == '(':
            chk.append(a)
        elif a == '[':
            chk.append(a)
        elif a == ')' or a == ']':
            if chk:
                t = chk.pop()
                if (a == ')' and t != '(') or (a == ']' and t != '['):
                    print("no")
                    return
            else:
                print("no")
                return
    if not chk:        # 남은 경우
        print("yes")
    else:
        print("no")
    return

text = ""
while True:
   
    arr = input().strip("\n") 
    if arr == '.':
        break
        
    text += arr
    
trr = text.split('.')
     
for t in trr:
    if t != "":
        check(t)                