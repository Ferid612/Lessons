a=1
c=1000
count = 0
while a <= c:
    b=1
    while b<=c: 
        if a**b == b**a and a !=b :
            count+=1
            print(a,b)
        b+=1  
    a+=1 
    
print(count)