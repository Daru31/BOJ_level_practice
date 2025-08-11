N = int(input()) 
for i in range(1, N): 
    l = list(map(int, str(i))) 
    if i + sum(l) == N: 
        print(i) 
        exit(0) 
print(0) 