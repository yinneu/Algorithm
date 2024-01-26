if __name__  == '__main__':
    a, b = map(int, input("").split(" "))

    if a > b:
        print('>')
    elif b > a:
        print('<')
    else:
        print('==')
    
    
    
