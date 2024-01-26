if __name__ == '__main__':
    
    t = int(input(""))
    nums = []
    
    for i in range(t):
        a, b = map(int, input("").split(" "))
        nums.append(a + b)
        
    for num in nums:
        print(num) 
        