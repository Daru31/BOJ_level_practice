N = int(input()) 
l = [] 
no = 0 
for i in range(N): 
    W = input().strip() 
    for j in W: 
        l += [j] 
        if l.count(j) > 1: 
            if l[-2] == l[-1]: 
                continue 
            elif l[-1] in l: 
                no += 1 
                break 
    l =[] 
            
print(N - no) 