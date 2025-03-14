N, K = map(int, input().split()) 
l = [i for i in range(1, N+1) if N%i == 0]
try: 
    print(l[K-1]) 
except: 
    print(0) 
