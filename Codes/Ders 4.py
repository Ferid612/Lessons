
#! Funksiyalar 


# result = factorial(n)
# print(f"{n} faktoriali = {result}")


# def funskiya_a_c(x): 
#     cavab = x + 2
#     return cavab
    

# print(funskiya_a_c(6))
# print(funskiya_a_c(8))
# print(funskiya_a_c(20))
# print(funskiya_a_c(25))
# a
# b
# c




#! Rekursiv funksiya

# n = int(input())

# def factorial(n):
    
#     if n == 0:
#         return 1
#     else:  # 5  factorial(4)  4* factorial(3)   3*factorial(2)  2 *factorial(1)  1* factorial(0) 1
#         return n * factorial(n - 1)


# print(factorial(5))

# list_a = (2, 4 ,5 )
# print(bool(list_a))




# def f(x):
#     if x < 0:
#         return
#     if x > 100:
#         return
#     print(x)


# f(-3)
# f(105)
# f(64)
# 64


#Funksiya hər şey return edə bilər
# def f():
#     return ['foo', 'bar', 'baz', 'qux']
 

# f()

# f()[2]

# f()[::-1]



# Python dict as an argument
# def f(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#     for key, val in kwargs.items():
#             print(key, '->', val)


# f(foo=1, bar=2, baz=3)



# Gonderilme tipi
# def f(a, b, c):
#     print(F'a = {a}')
#     print(F'b = {b}')
#     print(F'c = {c}')


# d = {'a': 'foo', 'b': 25, 'c': 'qux'}
# f(**d)



# Hem *args hem *kwargs

# """
# >>> def f(a, b, *args, **kwargs):
# ...     print(F'a = {a}')
# ...     print(F'b = {b}')
# ...     print(F'args = {args}')
# ...     print(F'kwargs = {kwargs}')
# ...

# >>> f(1, 2, 'foo', 'bar', 'baz', 'qux', x=100, y=200, z=300)
# a = 1
# b = 2
# args = ('foo', 'bar', 'baz', 'qux')
# kwargs = {'x': 100, 'y': 200, 'z': 300}

# """




# Multi list sending
# def f(*args):
#     for i in args:
#             print(i)


# a = [1, 2, 3]
# t = (4, 5, 6)
# s = {7, 8, 9}

# f(*a, *t, *s)



# Numune Concat
# def concat(prefix, *args):
#     print(f'{prefix}{".".join(args)}')


# concat('//', 'a', 'b', 'c')

# concat('... ', 'foo', 'bar', 'baz', 'qux')

# Canculyator funksiyasi yazin

#! Docstring



# def foo(bar=0, baz=1):
#     """Perform a foo transformation.

#     Keyword arguments:
#     bar -- magnitude along the bar axis (default=0)
#     baz -- magnitude along the baz axis (default=1)
#     """
#     return 5 * 6
 
 
# print(foo.__doc__)   


#! Lambda 
# x = lambda a : a + 10
# print(x(5))


# def func(a):
#     return  a + 10

# func = lambda a, y: a * y


# print(func(10,20))

# def test_func(a):
#     print(a+10000)
#     return a + 10000


# def myfunc():
#     return test_func


# x = myfunc()

# x(20)



# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)
# def mydoubler(a):
# return a*2
# print(mydoubler(11))



# def topla( *ededler, eded_1):
#     print("ededler:",ededler)
#     cem = sum(ededler)
#     print(cem)



# Calculator
# def hesabla(eded_1, eded_2, parametr ):    

#     birinci_eded = int(input('birinci_eded: '))
#     ikinci_eded = int(input('ikinci_eded: '))
#     netice = 0
#     if parametr == "+":
#         netice = birinci_eded+ikinci_eded
    
#     if parametr == "-":
#         netice = birinci_eded-ikinci_eded
      
#     if parametr == "*":
#         netice = birinci_eded*ikinci_eded
    
#     if parametr == "/":
#         netice = birinci_eded/ikinci_eded
      
#     return birinci_eded,ikinci_eded,parametr, netice



# parametr= input('parametr: ')

# eded_1, eded_2,parametr, netice = canculator(parametr)
# print(f"{eded_1} {parametr} {eded_2}  = {netice}")


# def test():
#   print("Salam dunyani")
  

#! OOP 

# usaq1 = {
#     "name":"hasan",
#     "surname":"aliyev",
#     "age":23
# }

# usaq2 = {
#     "name":"hasan",
#     "surname":"aliyev",
#     "age":23
# }


# usaq3 = {
#     "name":"hasan",
#     "surname":"aliyev",
#     "age":23
# }

# sinif ={
#     "parta_sayi":20,
#     "useqlar":[usaq1,usaq2,usaq3]
    
# }

# sinif["useqlar"][0]


# class Sinif:
#     def __init__(self, x,y): 
#         self.x = x
#         self.y =  y
#         print("constructor ise salindi")
        
#     def get_user_data(self):
#         print("x:",self.x)
#         print("y:",self.y)
#         return self.x


# object_a = Sinif(10,20)
# object_b = Sinif(30,40)


# object_a.get_user_data()
# object_b.get_user_data()

# print( object_a.x)         
        
        
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1)
