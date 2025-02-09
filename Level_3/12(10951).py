import sys 

while True: 
    line = sys.stdin.readline() 
    if not line: 
        break
    A, B = map(int, line.split()) 
    print(A + B) 

# sys.stdin.readline().split()가 EOF를 만나면, 빈 리스트([])를 반환함. 
# 빈 리스트를 정수로 매핑하는 것은 불가능하기 때문에, 
# 이를 예외처리 해주지 않고 코드를 실행하면 ValueError 가 발생하는 것. 

# <함수,EOF 시 반환값> 
# sys.stdin.readline(), "" (빈 문자열) 
# input(), EOFError 예외 발생 
# sys.stdin.read(), "" (빈 문자열) 
# sys.stdin.readlines(), [] (빈 리스트)