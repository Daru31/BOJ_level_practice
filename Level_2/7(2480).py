A, B, C = map(int, input().split()) 

if A == B == C: 
    print(10000 + A * 1000) 
elif A == B != C: 
    print(1000 + A * 100)
elif B == C != A: 
    print(1000 + B * 100)
elif C == A != B: 
    print(1000 + C * 100) 
elif A != B != C: 
    if A > (B and C): 
        print(A * 100) 
    elif B > (A and C): 
        print(B * 100) 
    elif C > (A and B): 
        print(C * 100)

# 왜 틀린걸까..
