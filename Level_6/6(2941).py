# 리스트로 한 글자씩 받아서 작업 - 어렵게도 생각했다. 
a = input() 
l = []
for i in a: 
    l += [i] 
    if l[-3:] == ['d', 'z', '=']: 
        l[-3:] = ' '
    if l[-2:] == ['c','='] or l[-2:] == ['c', '-'] or l[-2:] == ['d', '-'] or l[-2:] == ['l', 'j'] or l[-2:] == ['n', 'j'] or l[-2:] == ['s', '='] or l[-2:] == ['z', '=']: 
        l[-2:] = ' '
    
print(len(l))  

# 맨 처음에 이렇게 생각했다가 '그래도 실버 V 난이도인데..' 싶어서 철회했던 방법 
croatian_alphabets = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = input().strip()

for alphabet in croatian_alphabets:
    word = word.replace(alphabet, "*")  

print(len(word))