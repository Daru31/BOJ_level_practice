import sys 

T = int(sys.stdin.readline()) 
for i in range(T): 
    A, B = map(int, sys.stdin.readline().split()) 
    print("Case #"+str(i+1)+": "+ str(A+B))
    
# '+' 연산자는 같은 type 끼리만 가능, ',' 연산자는 다른 타입끼리도 가능. 