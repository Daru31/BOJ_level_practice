N, M = map(int, input().split()) 
basket = [0] * N 
print(map(str, basket))
for _ in range(M): 
    i, j, k = map(int, input().split()) 
    basket[i-1:j] = [k] * (j-i+1)
    
print(' '.join(map(str, basket)))  
# 1. map(str, basket)으로 basket 리스트의 각 요소에 str() 함수 적용 = list -> map  
# 1 + @. map()은 변환 결과를 메모리에 저장하지 않고, 필요할 때 '지연 평가(lazy evaluation)' 방식으로 변환 수행 -> 그래서 print()해도 값이 나오지 않았던 것. 
# 2. 각 요소를 구분하는 '구분자'를 공백(' ')으로 대체 + 대괄호 삭제 = map -> str 
# 다음 단계에서 서술할 *basket 으로 언패킹 하는 방식을 쓰도록 하자. 