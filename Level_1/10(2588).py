one = int(input()) 
two = str(input()) # 슬라이싱을 위한 string 변환 

# 곱셈 세로셈 계산 후, 과정 및 결과 출력 
three = one*int(two[2]) 
four = one*int(two[1])
five = one*int(two[0])
print(three) 
print(four) 
print(five) 
print(three + four*10 + five*100) 
