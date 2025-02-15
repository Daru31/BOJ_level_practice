N, M = map(int, input().split()) 
basket = list(range(1, N+1)) # range를 통한 등차수열 생성 -> range 또한 지연 평가를 사용하는 type 이므로 list로 변환. 

for _ in range(M): 
    i, j = map(int, input().split()) 
    change = basket[i-1] 
    basket[i-1] = basket[j-1] 
    basket[j-1] = change 
    
print(*basket) 
# * = 언패킹(unpacking) : iterable 객체의 각 요소를 개별적인 인자로 풀어서 전달. 
#  print(' '.join(map(str, basket))) 을 완벽히 대체. 