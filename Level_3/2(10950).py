# 최종 결과 
T = int(input()) 
result = ""

for i in range(0, T): 
    A,B = map(int, input().split())
    result += str(A+B) + "\n"
    
print(result) 

# 축약본 
T = int(input()) 

for i in range(0, T): 
    A,B = map(int, input().split()) # 알아서 input을 받게 된다. 
    print(A+B) 