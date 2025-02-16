stu = list(range(1,31))  
yes = []

for i in range(28): 
    n = int(input()) 
    if n in stu: 
        yes.append(n) 
        
no = set(stu) - set(yes) # set = list 연산 
no = list(no) 
no.sort() 
print(no[0]) 
print(no[1]) 
