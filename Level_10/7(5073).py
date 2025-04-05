while True: 
    l = list(map(int, input().split())) 
    if 0 in l: 
        break 
    elif max(l) >= sum(l) - max(l): 
        print('Invalid') 
    elif len(set(l)) == 1: 
        print('Equilateral') 
    elif len(set(l)) == 2:
        print('Isosceles') 
    elif len(set(l)) == 3: 
        print('Scalene') 
     