l = [] 
for i in range(10): 
    n = int(input()) 
    n %= 42 
    l += [n] 
    if l.count(n) > 1: 
        l.remove(n)  

print(len(l)) 