
#! Syntax

# variable_a = 12
# print(variable_a)

# a = b = c = 300

# print(a)
# print(b)
# print(c)



#! Unboxing
# list_a = [2,3,4,5]
# a, b, c, d = list_a

# print(a)
# print(b)
# print(c)
# print(d)


# x = 10
# x += 20 
# x -= 10

# x = x *10

# x//=10


#! Case Types
# age = 1
# Age = 2
# aGe = 3
# AGE = 4
# a_g_e = 5
# _age = 6
# age_ = 7
# _AGE_ = 8

# vairable =5

# [A-Z]  [a-z] [0-9]  _ 
# print(age, Age, aGe, AGE, a_g_e, _age, age_, _AGE_)


# camelCase
# PascalCase  Upper camelCase
# snake_case
# kabab-case

# PEP8


# Pascal Case 
# Upper CamelCase
# UserLastName = ""
# UserPassword = ""
# User =""


# Variable name snake_case user_password user_lastname
# class yaradirsizsa PascalCase



#! KEYWORDS  

# for = ""

# help("class")


# None = ""

# Keywords


# print(
    
#     help("False ")
    
#     )


#! Isclose 
# x = 1.1 + 2.2
# print(x)
# print(x == 3.3)

# from math import isclose
# x = 1.1 + 2.2
# print( isclose(x,3.3))

# x y arasindaki ferq 20 faizden den cox deyilse bunlari beraber kimi qebul et
# print( isclose(6, 7, rel_tol=0.2))


#! Boolean cheking 
# print("a" <  "A")
# print(ord("A"))
# print(ord("a"))

# print( "SalamT" < "SalanT")

# print([5,6,7]< [8])




#! Data types
# integer int
# a = 20
# string str
# b = "20"
# boolean bool
# c = True

#None type
# x = None

# float
# e = 2.5
#  complex
# d = 5j


# print(type(a))
# print(type(b))
# print(type(c))
# print(type(e))
# print(type(d))

# number_a = int(input("Daxil edin: ")) 
# print(type(number_a))

# print("senin girdiyin deyer:", number_a)


#! all
# variable_b = (True, True, True)
# print(all( variable_b))

# tuple_a  = ( False, True, 8!=10, 5>2)
# print(all(tuple_a))
# print(any(tuple_a))

#! Isinstance
# number = 42  
# Object orianted programing  - OOP
# print(type(number))
# validation_conditions = (isinstance(number, int),number % 2 == 0,)
# print(all(validation_conditions))

#! Callabe
# number = 24
# for a in number:
    # print(a)
    
# number
# print(   callable(print)   )

# a = int(number)

#! Short life cycle
# number_a = "salam" and "sagol" and "" and "Yox"

# number_b = 2 > 4 and 2
# print(number_b)


# default_country = "Canada"

# country = "" or default_country

# print(country)

# deyisgen = "12"


# var_a = 0 and 3
# print(var_a)
# number = 0


    


#! Is keyword
# x = y
# y = x

# print(id(x))
# print(id(y))

# y = 1001

# print(x is y)


#! In keyword

# print(1 not in list_a)


#! IF ELIF

# if number:
#     print("true qayitdi")
# else:
#     print("false qayitdi")


# ifade = ""

# if ifade: 
#     print("Working")
# else:
#     print("Not working")

# print ( bool(ifade))


# netice = "musbet" if number_a>0 else "menfi" if number_a<0 else "sifir" 
# print(netice)

# number_b = "23"



#! If with short life cycle
# if number_b == 23 or not number_b < 59:
#     print("Sert odendi")
# else:
#     print("sert odenmedi")

# if len(list_a):
#     print("Bize true qayitdi")
# else:
#     print("Bize false qayitdi")
# print(tuple(range(0,100)))
    




#! Input with Numbers


# variable_a=""
# number_1 = int(input("number_1: "))
# number_2 = int(input("number_2: "))


# if number_1>number_2:
#     variable_a = f"{number_1} {number_2} den boyukdur"
# else:
#     variable_a = f"{number_2} {number_1} den boyukdur"


# variable_a = f"{number_1}  {number_2} den boyukdur" if number_1>number_2  else f"{number_2} {number_1} den boyukdur"
# variable_a = number_1 > number_2 and f"{number_1} {number_2} den boyukdur" or f"{number_2} {number_1} dem boyukdur"

# print(variable_a)




#! Random library
# import random
# x= random.randrange(1, 1077)
# print(x)

# count = 10000000

# i = 0
# cem = 0
# while i < count:
#     x  = random.randrange(1,7)
#     cem += x 
#     i += 1        
    

# print(cem/count)
    
    
    