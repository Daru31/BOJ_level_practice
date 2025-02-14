result = 0 
where = 0 

for i in range(1, 10): 
    l = int(input()) 
    if l > result: 
        result = l 
        where = i 
        
print(result) 
print(where) 
    