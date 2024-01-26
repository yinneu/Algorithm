if __name__ == '__main__':
    
    a, b = map(int, input("").split(" "))
    
    print(abs(a - b))
    
    # result = 0
    
    # # 부호가 같음 (절댓값: 큰 값 - 작은 값)
    # if a < 0 and b < 0:
    #     if a < b:            
    #         result = -(a - b)
    #     else:
    #         result = -(b - a)    
    # elif a > 0 and b > 0:
    #     if a > b:
    #         result = a - b
    #     else: 
    #         result = b - a  
    # # 부호 다름
    # elif a < 0 and b > 0:
    #     result = b - a   
    # else:
    #     result = a - b
        
    # print(result)
    
    # 두 사이의 어떤 값이든지 빼고 절댓값을 구하면 두 값의 차이가 나옴,,,