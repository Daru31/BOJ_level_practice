n = int(input())
paper = [[0 for _ in range(100)] for _ in range(100)] 
sum = 0 
for _ in range(n): 
    x, y = map(int, input().split())
    for i in range(x, x + 10): 
        for j in range(y, y + 10): 
            if i >= 100 or j >= 100: 
                break
            paper[i][j] = 1
for row in range(100):
    sum += paper[row].count(1)

print(sum) 
# 전부 0으로 채워진 100x100 의 행렬이 있고, 전부 1로 채워진 10x10 행렬로 100x100 행렬을 교체한다는 느낌. 