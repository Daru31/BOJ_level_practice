N = int(input()) 
for i in range(0, N*2-1): 
    if i < N: 
        print(' '*(N-1-i) + '*'*(2*i+1) + ' ') 
    elif i >= N: 
        print(' '*(i-(N-1)) + '*'*((N*2-1)-(2*i-(N*2-2))) + ' ') 