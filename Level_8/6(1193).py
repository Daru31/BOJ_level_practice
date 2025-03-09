X = int(input()) 
f = 0 
i = 0
while True: 
    i += 1
    f += i # 팩토리얼 구현 
    if f >= X: 
        result = abs(X-(f-i))
        break 
if i % 2 == 0: 
    print(str(result)+'/'+str(i-result+1))
else: 
    print(str(i-result+1)+'/'+str(result)) 
# 규칙에 따라 순서 지정 