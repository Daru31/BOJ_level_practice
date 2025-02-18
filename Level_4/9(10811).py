N, M = map(int, input().split()) 
l = list(range(1, N+1)) 
for _ in range(M): 
    i, j = map(int, input().split()) 
    if i == 1: 
        l[i-1:j] = l[j-1::-1] 
    else: 
        l[i-1:j] = l[j-1:i-2:-1] 
    
print(*l) 
# 리스트 역순 : step 부분을 음수로 하고, start 와 end 부분을 서로 바꾼 후 리스트 조건에 맞게 수정. 
