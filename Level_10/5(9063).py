import sys
input = sys.stdin.readline

N = int(input()) 
xc = [] 
yc= []
for i in range(N): 
    x, y = map(int, input().split()) 
    xc.append(x) 
    yc.append(y) 
print((max(xc)-min(xc))*(max(yc)-min(yc))) 

# sys.stdin.readline & append : O(N) 
# input & += [] : O(N^2) 