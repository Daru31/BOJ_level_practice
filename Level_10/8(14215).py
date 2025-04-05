a, b, c = map(int, input().split()) 
l = [a, b, c] 
if max(l) < sum(l)-max(l): 
    print(sum(l)) 
else:  
    print((sum(l)-max(l))*2-1)
