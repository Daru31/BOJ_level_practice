while True:
    a, b = map(int, input().split()) 
    if a == b: 
        break
    elif a<=b and b%a == 0: 
        print('factor') 
    elif a>=b and a%b == 0: 
        print('multiple') 
    else: 
        print('neither') 