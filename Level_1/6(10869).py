A, B = input().split() 
A, B = map(int, (A, B)) # map(func, *iterables) : 각 반복 가능한(iterable) 요소에 대해 function 수행 

print(A+B, A-B, A*B, A//B, A%B, end='\n') 
