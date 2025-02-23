dic = {'A+' : 4.5, 'A0' : 4.0, 'B+' : 3.5, 'B0' : 3.0, 'C+' : 2.5, 'C0' : 2.0, 'D+' : 1.5, 'D0' : 1.0, 'F' : 0.0}
plus = 0 
score = 0
for i in range(20): 
    a = list(input().split()) 
    if a[2] == 'P': 
        a[1] = 0
    plus += float(a[1]) * dic.get(a[2],0) 
    score += float(a[1]) 
    
print(plus/score)