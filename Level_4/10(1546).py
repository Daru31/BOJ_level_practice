N = int(input()) 
S = list(map(int, input().split())) 
M = max(S) 
for i in range(N): 
    new =  S[i] / M * 100 
    S[i] = new  
    
print(sum(S)/N) 
