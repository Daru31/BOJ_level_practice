a = input() 
if len(a)%2 == 0: 
    if a[0:len(a)//2] == a[:len(a)//2-1:-1]: 
        print(1) 
    else: 
        print(0) 
else: 
    if a[0:len(a)//2] == a[:len(a)//2:-1]: 
        print(1) 
    else: print(0) 