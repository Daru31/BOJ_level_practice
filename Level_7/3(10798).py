a = [input() for i in range(5)] 
b = []
for i in range(15): 
    for j in range(5): 
        try: 
            b += [a[j][i]] 
        except IndexError: # 에러 ㅈ까
            continue 
        
print("".join(b)) 