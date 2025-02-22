import sys
from collections import Counter

a = sys.stdin.readline().strip().lower()  # 입력받고 소문자로 변환
counter = Counter(a)  # 각 문자의 개수를 한 번에 계산 (O(N))

max_count = max(counter.values())  # 최빈 문자 개수 (O(N))
max_chars = [ch for ch, cnt in counter.items() if cnt == max_count]  # 최빈 문자 찾기 (O(N))

print('?') if len(max_chars) > 1 else print(max_chars[0].upper())  # 최빈 문자가 1개면 그것의 대문자 출력, 아니면 '?' 출력 

# counter 안쓰고 성공한 코드 - 분석해보자. 
word = input().upper()
my_dic = {}
my_list = []
for i in word:
    my_dic[i] = my_dic.get(i,0) + 1
max_value = max(my_dic.values())
for key, value in my_dic.items():
    if value == max_value:
        my_list.append(key)
if len(my_list) > 1:
    print("?")
else:
    print(my_list[0])
