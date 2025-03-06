# 층마다 칸이 증가하는 규칙 
# 1 -> 1 + 6*1 = 7 -> 7 + 6*2 = 19 -> 19 + 6*3 = 37 -> ... 

N = int(input())
room = 1 # 각 칸의 개수이자 최댓값 
num = 1 # 규칙을 위해 1씩 증가하는 수 

while N > room: # 입력값이 room 보다 작으면 반복문 중단 
    room += 6 * num
    num += 1
print(num) 
