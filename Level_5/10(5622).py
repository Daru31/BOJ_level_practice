A = B = C = 2 
D = E = F = 3 
G = H = I = 4 
J = K = L = 5
M = N = O = 6
P = Q = R = S = 7 
T = U = V = 8 
W = X = Y = Z = 9 

a = input() 
result = 0 
for i in range(len(a)): 
    result += globals().get(a[i]) + 1 # globals() : 문자(str)를 그것과 같은 이름의 변수값으로 받아옴. 
    # locals() :  함수 내부에서 사용하는 globals() 
print(result) 

# 이게 정석 같음. 
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
ret = 0
for j in range(len(a)):
    for i in dial:
        if a[j] in i:
            ret += dial.index(i) + 3
print(ret)