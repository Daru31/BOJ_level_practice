N = int(input()) 
l = list(map(int, input().split())) 
result1 = 0
for i in range(len(l)): 
    if l[i] == 1: 
        continue
    result = []
    for j in range(1, l[i]+1): 
        if l[i]%j == 0: 
            result += [j]
    if result == [1, l[i]]: 
        result1 += 1 
