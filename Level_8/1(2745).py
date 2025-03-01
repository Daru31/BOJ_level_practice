import sys 
N, B = sys.stdin.readline().strip().split()   
conv = 0 
dic = {chr(i):i-55 for i in range(65,91)}  
for i in range(len(N)): 
    if N[i] in dic: 
        val = dic.get(N[i]) 
    else: 
        val = int(N[i]) 
    conv += val*(int(B)**(len(N)-i-1)) 
print(conv) 

# int(n, base) : base 진법의 숫자 n을 10진법으로 변환해줌. 
n, b = input().split()
print(int(n, int(b))) 
# 단 두줄 컷;; 