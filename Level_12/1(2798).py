n, m = map(int, input().split()) 
l = list(map(int, input().split())) 
r = [] 
for i in range(n): 
    for j in range(n): 
        for k in range(n): 
            if i == j or j == k or k == i: 
                continue 
            r.append(l[i]+l[j]+l[k]) 
for i in range(m): 
    if m-i in r: 
        print(m-i) 
        break 