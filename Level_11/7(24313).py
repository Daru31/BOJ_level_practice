import sys 

a1, a0 = map(int, input().split()) 
c = int(input()) 
n0 = int(input()) 

for n in range(n0, 101): 
    if not a1*n + a0 <= c * n: 
        print(0) 
        sys.exit(0) 
print(1) 