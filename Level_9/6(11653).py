# i를 불필요하게 증가시키는 코드. 비효율적이다. 
N = int(input()) 
i = 2 
while N != 1: 
    if N%i != 0: 
        i += 1 
        continue
    N = N/i 
    print(i) # took 1432ms 

# 한번 나눈 후 for문을 빠져나와 다시 2부터 탐색 -> while 합연산보다 for문이 더 빠르다. 
n = int(input())
while n != 1:
    for i in range(2, n+1):
        if not n%i:
            print(i)
            n = n//i
            break # took 976ms
