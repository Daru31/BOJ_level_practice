while 1: 
    n = int(input()) 
    if n == -1: 
        break 
    l = [i for i in range(1, n) if n%i == 0]  
    if sum(l) == n: 
        l = map(str, l)
        print(n, '=', ' + '.join(l)) 
    else: 
        print(n, 'is NOT perfect.') 
