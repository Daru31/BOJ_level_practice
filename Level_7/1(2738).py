N, M = map(int, input().split()) 
a = [] 
b = [] 
for _ in range(N): 
    a += [input().split()] # list(): 데이터를 리스트 형식으로만 전환 / []: 데이터를 리스트 형식으로 전환 및 대괄호 생성 
for __ in range(N): 
    b += [input().split()] 

for i in range(N):  
    for j in range(M): 
        print(int(a[i][j]) + int(b[i][j]), end=" ") 
        if j == M-1: # 없어도 된다. 
            print() 