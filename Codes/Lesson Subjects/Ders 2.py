
#! Data types
# x = 0    # int  # integer 
# y = 2.8  # float  
# z = 1j   # complex
# a = "salam" # string 
# b = True # boolean
# c = None # Nonetype

# print(type(x))
# a = complex(x)
# print(a)
# print(type(a))

# a  = 23.
# print(type(a))


# a = 20
# b = 2.4
# c = 30
# d = None

# print(a<d)



#convert from int to float:
# x = "100"
# x = int(x)


# print(type(x))

 
# a = float(x)
# print(a)
# print(type(a))

#convert from float to int:
# b = int(y)

#convert from int to complex:
# c = complex(x)

# print(a)
# print(b)
# print(c)

# print(type(a))
# print(type(b))
# print(type(c))



# a = 23 
# b = int(input("B ni  daxil edin: "))

# print(a>b)


#! Lists

# c = [2,4,6,8,10]

#   0,1,2,3,4 
# print(c)
# print(type(c))

# print(  c[-12]    )

# index 

# var_a = [ 2, 4, 20]
#         0   1 2
# 0 2
# 1 4
# 2 20

# print(var_a)
# var_b =  ["salam", "necesen", "neynirsen"]
# print(var_b)


# print(var_b[1])
# print(var_a[-1])



# print(type(var_b))


# var_a = [1, 2, 3, 4, 5]
# var_b = [2, 4, 5, 6, 8]

# print(var_a)
# # print(type(var_a))

#Length 
# print(  len(var_b)  )

# print(len(var_a))
# print( var_a[-5] )

# var_a[0] = 12
# var_a[2] = 23

# print(var_a)


#! Slice 
# var_a = [1, 2, 3, 4, 5,6,7,8,9,10]
# list_c = var_a[:4]
# list_c = var_a[::-1]

# print(  list_c    )

# var_a = 101*[1]
# print(var_a)

# var_a = ["a","b","c","d"]
# var_b = [2,4,5,6,8]

# var_c = var_a + var_b
# print(var_c)

# list_a = [1,2,3,4,5,6,7,8,90]
# list_b = [6,7,8,290]

# print(  max(list_a)   )
# print(  min(list_b))
# print(  sum(list_a))


#! Append

# list_a = [2,3,4,5,6] 

# list_a.append(12)
# list_a.append(13)
# list_a.append(14)
# print(list_a)



# list_a  = [[1,3,5,7,9,11], [2,4,6,8,10] ]
# print(list_a[1][3])



#! COPY
# list_a = [2,3,4,5,6] 
# list_b = list_a.copy()

# print(id(list_a))
# print(id(list_b))


# list_b[0] = 20
# list_b[1] = 35
 
# print(list_b)
# print(list_a)

# list_b.append(1221)
# list_b[0] = True

# print(list_a)
# print(list_b)

# list_b = list_a.copy()
# list_b = list_a.c()

# list_b[2] = 1000

# print(list_a)
# print(list_b)




#! Extend
# list_a = [2,3,4.4,5,6,2,12] 
# list_b = [23,23,4,2321,12] 

# list_a = list_a + list_b
# list_a.extend(list_b)
# print(list_a)

#! Index
# print( list_a.index(2)  )
# Listin icinde verilen ededin butun indekslerini tapan proqram yazin!

#! Insert 
# list_a = [1,2,3,4,5]

# list_a.insert(5,13)
# print(list_a)

# list_a.insert(5,"Salam")

# print(list_a)
# print(list_a.pop())
# print(list_a)
# print(list_a.pop())
# print(list_a)

# print(list_a)
# list_a.remove(4)
# print(list_a)

# list_a = [1,2,3,4,5,2,2,2,2,2]
# var_a = list_a.count(2)
# print(var_a)





# list_a = [1,2,3,4,5,2,2,2,2,2]
# list_a.insert(5,13)
# print(list_a.pop())
# list_a.remove(4)
# var_a = list_a.count(2)

# list_a  = list( range(1, 100, 2) )

    
#! Range Lazy memory

list_a =  range(20, 410000)
# list_a =  range(20, 41000000, 2)
# list_a =  range(20, 41000000, 2)
# list_a =  range(20, 41000000, 2)
# print(list_a)
# list_a = list_a[::3]
# print(list_a)

# print(list_a)
# x = range(21,200)[5]
# print(x)
# print(type(x))




# y = x[::3]
# print(y)

# print(list(range(3,20,3)) + list(range(20,3,-3)) )
# a= 20
# b = 3
# k =1
# d = list(range(a,b,-3))
# print(d)
# a,b 




#! LOOPS
#! Iterate etmek 
#! Iterable object


# ededler = [1,2,3,4,5,6,7,8,9]

# for a in ededler:
#     print("a:", a)

# for eded in ededler:
#     print(eded*33)

# [print(eded) for eded in [1,2,3,4,5,6,7,8,9]]    

# adlar = ["Eziz","Ramiz","Lale","Baleeli"]

# for ad in adlar:
#     print(ad)
    
#! Range


# for item in range(1,151):
#     print(item)



adlar = ["Eziz","Ramiz","Lale","Baleeli"]
# print(len(adlar)) #-- listlerin uzunlugunu olcusunu length 

for item in range(len(adlar)):
    print(item, adlar[item])

# ededler = [1,2,3,4,5,6,7,8,9]
# for i in range( len(ededler)  ):
#     print(i, ededler[i])
    



#! Nəzrinlə burada qaldıq 


# print(len(a))


# a = "Hello, World!"
# for x in a:
#   print(x)



# input_a = ""
# while input_a !=  "Sagol":
#     input_a = input()
#     print("musteri input "+ input_a)


# list_a = [1,2,3,4,65,7,8,8,90]

# i = 0
# while i < len(list_a):
#     print(list_a[i])
#     i+=1
    


# while True:
#     ad = input("Adinizi daxil edin: ")
#     print(f"Salam {ad}")
#     if ad == "Mustafa":
#         break

# while list_a:
#     print(list_a.pop())

# list_a = [2,3,4,5,6] 
   
# i = 0
# while i < len(list_a):
#     print(list_a[i])
#     i = i+ 1


# list_a = [2,3,4,2]
# print(list_a)
# list_a = set([2,3,4,2])
# print(list_a)

a= 200

if a > 10:
    b = 20
elif a > 5:
    b = 30
else:
    b = 40




# b = 20 if a > 5 else 30 if a<3 else 40

# a = 9
# print(a**(1/2))
# 81 ustu 0.5
# 81 kokalti 9 
