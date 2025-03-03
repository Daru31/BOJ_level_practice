import sys 
N, B = map(int, sys.stdin.readline().strip().split()) 
conv = [] 
dic = {i-55:chr(i) for i in range(65,91)} 
while True: 
    if N%B in dic: 
        conv += [dic.get(N%B)]
    else: 
        conv += [str(N%B)] 
    N = N//B 
    if N == 0: 
        break 
print("".join(conv[::-1])) 