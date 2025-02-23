import sys 
from collections import Counter 

a = sys.stdin.readline().strip().lower() # 입력받고 소문자로 변환. 
counter = Counter(a) # Counter : 각 문자의 등장 횟수를 세어 dic(key:value) 형태로 반환하는 객체.  

max_count = max(counter.values()) # Value에 해당하는 문자 등장 횟수의 최댓값을 반환. 
max_chars = [] 
for ch, cnt in counter.items(): # ch, cnt == key, value 
    if cnt == max_count: 
        max_chars += [cnt] 
if len(max_chars) > 1: 
    print('?') 
else: 
    print(max_chars[0].upper()) 


# 최적화 (리스트 컴프리헨션) 
import sys
from collections import Counter

a = sys.stdin.readline().strip().lower()  
counter = Counter(a)  

max_count = max(counter.values())  
max_chars = [ch for ch, cnt in counter.items() if cnt == max_count]  

print('?') if len(max_chars) > 1 else print(max_chars[0].upper())  


# counter 안쓰고 성공한 코드 
word = input().upper()
my_dic = {}
my_list = []
for i in word:
    my_dic[i] = my_dic.get(i,0) + 1 # get(key, std)으로 my_dic 을 채워나감. my_dic 에 해당 i(key)가 없으면 std값(0) 지정, 있으면 그것의 value 반환. +1 로 실질적 등장 횟수 지정.  
max_value = max(my_dic.values())
for key, value in my_dic.items(): # 위의 max_chars 와 동일한 작업. 
    if value == max_value:
        my_list.append(key)
if len(my_list) > 1:
    print("?")
else:
    print(my_list[0])


# 원래 리스트로 값을 저장한 다음 count 객체를 통해 횟수를 세는 코드를 작성했으나, 반복 과정이 중첩되어 시간복잡도가 O(N^2)이 되어 시간초과 발생. 
# 딕셔너리는 key value 지정 작업이 하나의 작업이기 때문에, 딕셔너리로 같은 작업을 수행하면 과정이 중첩되지 않아 시간초과 해결 가능. 
