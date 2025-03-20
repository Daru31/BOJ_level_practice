# 내 방식 : input 다 받고 이 중에 없는 값 한번 더 받기 
a = [] 
b = []
for i in range(3): 
    m, n = map(int, input().split()) 
    a += [m] 
    b += [n] 
for i in range(4): 
    if a.count(a[i]) != 2: 
        a += [a[i]] 
    if b.count(b[i]) != 2: 
        b += [b[i]] 
print(a[3], b[3]) 

# 없으면 더하고, 있으면 빼는 방식 
x=[]
y=[]
for i in range(3):
    a,b=map(int,input().split())
    if a in x:
        x.remove(a)
    else:
        x.append(a)
    if b in y:
        y.remove(b)
    else:
        y.append(b)
print(x[0],y[0]) 

# 브?루?트 포?스 
import sys
a,b,c,d,e,f=map(int,sys.stdin.read().split())
if a==c: print(e,end=' ')
elif a==e: print(c,end=' ')
elif c==e: print(a,end=' ')
if b==d: print(f,end=' ')
elif b==f: print(d,end=' ')
elif d==f: print(b,end=' ')