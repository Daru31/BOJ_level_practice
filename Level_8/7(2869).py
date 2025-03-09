A, B, V = map(int, input().split()) 
r = (V-A)//(A-B)
if 0 < (V-A)/(A-B) < 1: 
    r = 1
elif (V-A)%(A-B) != 0: 
    r = (V-A)//(A-B) + 1
print(r+1) 
# 반복문의 소중함을 깨닫게 되었다. 