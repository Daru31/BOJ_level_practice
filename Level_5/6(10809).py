S = input() 

a = [chr(i) for i in range(ord('a'), ord('z') + 1)] # 알파벳의 아스키코드는 1씩 차이남. 
for j in range(26): # 알파벳 개수 
    if a[j] in S: 
        a[j] = S.index(a[j]) 
    else:  
        a[j] = -1 

print(*a) 