# 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다.

# Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다. 
# 단, 이때는 맨 끝의 개행문자(\n)까지 같이 입력받기 때문에(char처럼 눈에 보인다.)
# 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다. 

import sys 

T = int(sys.stdin.readline())
for i in range(T): 
    A,B = map(int, sys.stdin.readline().split())   
    print(A+B) 