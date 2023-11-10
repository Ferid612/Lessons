#! Numene 1 Start
"""x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

print(x)
print(y)
print(z)
"""
#! Numune 1 END



#! Numene 2 Start
"""x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))"""
#! Numene 2 End

# print(5j*5j)


# english_levels = {
#     "a1":"beginner",
#     "a2":"elemetry",
#     "c1":"pre-intermadate",
#     "b1":"pre-intermadate12",
# }




# list_a = [2,3,4,2]
# print(list_a)
# list_a = set([2,3,4,2])
# print(list_a)


# variable = None


# Onlayn dersler: Multiline Strings


# myTuple = ("John", "Peter", "Vicky")

# x = "#".join(myTuple)

# print(x)


# string_a = "Salam BAKI NECESEM"
# list_a = string_a.startswith("BAKI",6,8)


# print(list_a)






# def hesabla(eded_1, eded_2, parametr ):    
#     netice = 0
#     if parametr == "+":
#         netice = eded_1/+ eded_2
#         print(f"{eded_1} + {eded_2} =  {netice}")

#     elif parametr == "-":
#         netice = eded_1 - eded_2
        
#         print(f"{eded_1} - {eded_2} =  {netice}")
    
#     elif parametr == "*":
#         netice = eded_1*eded_2
#         print(f"{eded_1} * {eded_2} =  {netice}")
    
#     elif parametr == "/":
#         netice = eded_1/eded_2
        
#         print(f"{eded_1} / {eded_2} =  {netice}")

#     return netice


# birinci_eded =  12
# parametr = "*" 
# ikinci_eded = 34

# print("netice:",hesabla(birinci_eded,ikinci_eded,parametr))


# def topla( *ededler, eded_1):
#     print("ededler:",ededler)
#     cem = sum(ededler)
#     print(cem)


# topla(2,3,5,20202,20)

def faktorial(x):
    if x == 0:
        return 1
    else:
        return x*faktorial(x-1)   

print(faktorial(5))