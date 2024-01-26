#https://www.acmicpc.net/problem/10951
if __name__ == '__main__':
    
    result = []

    while True:
        try:
            a, b = map(int, input("").split(" "))
            result.append(a + b)           
        except:
            break
            
    for n in result:
        print(n)
        
# 입력이 없는데, 입력을 받으려고 하는 경우 => 런타임에러 (EOFError) 뜸
# 예외 처리해야함,,