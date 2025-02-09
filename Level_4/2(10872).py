import sys 

N, X = map(int, sys.stdin.readline().split())  
A = list(map(int, sys.stdin.readline().split())) 

for i in range(N):  
    if A[i] < X: 
        print(A[i], end=" ") # end="\n"이 대체되어서 한줄로 출력됨. 
