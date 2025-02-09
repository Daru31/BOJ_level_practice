import sys 

N = int(sys.stdin.readline()) 
L = list(map(int, sys.stdin.readline().split())) 
v = int(sys.stdin.readline()) 

print(L.count(v)) 

# 서버 프로그램이 알아서 L에 N회 input을 할당함. 