A, B, C = input().split() 
A, B, C = map(int, (A, B, C)) 

print((A+B)%C, ((A%C)+(B%C))%C, (A*B)%C, ((A%C)*(B%C))%C, end='\n') 
# 신기하다 
