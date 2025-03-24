l = [int(input()) for i in range(3)] 
if sum(l) != 180: print('Error') 
elif l == [60, 60, 60]: print('Equilateral') 
elif sum(l) == 180 and 2 in [l.count(i) for i in l]: print('Isosceles') 
elif sum(l) == 180 and l[0] != l[1] != l[2]: print('Scalene') 
# 작품명 : iterable을 좋아하는 사람의 발악 

# set()으로 더 최적화 할 수 있다. 
l = [int(input()) for _ in range(3)] 
if sum(l) != 180: print('Error') 
elif len(set(l)) == 1: print('Equilateral') 
elif len(set(l)) == 2: print('Isosceles') 
else: print('Scalene') 