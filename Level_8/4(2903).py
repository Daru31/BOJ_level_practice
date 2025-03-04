N = int(input()) 
l = [['0','0'], ['0','0']] 
for i in range(N): 
    l[0] = '0'.join(l[0]) 
    l[1] = '0'.join(l[1]) 
print(len(l[0]) * len(l[1])) 