a = [list(map(int, input().split())) for i in range(9)] 
l = [] 
for i in range(9): 
    l += list(str(max(a[i])).split()) 
print(max(l)) 
for j in range(9): 
    if int(max(l)) in a[j]: 
        print(int(l.index(max(l)))+1, int(a[j].index(int(max(l))))+1) 
