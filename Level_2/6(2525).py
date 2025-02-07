A, B = map(int, input().split()) 
C = int(input()) 
minute = B + C 
hour = A + (B+C)//60 

if minute >= 60: 
    minute -= 60*(minute//60) 
if hour >= 24: 
    hour -= 24*(hour//24) 
    
print(hour, minute) 

# ㅈㄴ 삽질함 ;;
