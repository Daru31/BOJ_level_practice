import sys 
import os 

N = int(sys.stdin.readline()) 
width = os.get_terminal_size().columns # 환경마다 다른 터미널 크기를 불러와서 맨 오른쪽으로 정렬함. 
for i in range(N): 
    print(f'{'*'*(i+1):>{width}}')  
    
# 함수에서 괄호()의 여부는 함수를 실행하냐, 속성만 가져오냐의 차이. 
# line 5의 .columns 는 정수형 객체임 -> 괄호 붙여서 '호출'하면 오류남. 
# 얘 왜 백준에서 오류남? 