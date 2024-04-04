
#! Funksiyalar 


# def mehsul_al(x):
#     print(f"{x} mehsulu alindi")   


# def cemini_tap(x , y):
#     cem = x + y
#     return cem


# netice = cemini_tap(3,5)
# netice_2 = cemini_tap(8,10)
# a  = 1,2,3 
# b = 1,2,4
# c = 2,4,7
# d = 5,6
# list_a [a,b,c, d]

# list_a = [[1,2,3],[1,2,4],[2,4,6]]

# arr = np.array([12,3][2,4][4,5]])

# a = 12,3,2,4,4,5 fdsfdskfds
# c= 13

# def mehsul_al(mehsul_adi="Corek", qiymet=40):
#     print(f"{mehsul_adi} mehsulu {qiymet} qepiye alindi")   


# mehsul_al(mehsul_adi="Yumurta", qiymet=20)



# def kvadratini_tap(*x):
#     list_a = []
#     for i in x:
#         list_a.append(i**2)
#     return 1,True,"Salam", 2.3, 5j, [22,1,12,1,2]


# netice_1,*netice_2 = kvadratini_tap(4,3,1,12,32,2,3121,31,32)



# print(netice_1)
# print(netice_2)
# list_a = [1,2,3,4,5,5,6,787]

# a, *b = list_a
# print(a)
# print(b)



# def funksiya_a(item,item_3 ,  item_2 = "Mehemmed" ,  ):
#     print(f"Salam {item}")
#     print(f"Salam {item_2}")
#     print(f"Salam {item_3}")
    
    
    
# def canculator(number_1, number_2, operator):
#     if operator == "+":
#         return number_1 + number_2        
    
#     elif operator == "-":    
#         return number_1 - number_2
    
#     elif operator == "*":
#         return  number_1 * number_2
    
#     elif operator == "/":
#         return number_1 / number_2


# def duzbucaqlidirmi(a,b,c):
#     if (c**2 == a**2 + b**2) or (a**2 == c**2 + b**2) or (b**2 == a**2 + c**2) :
#         print("Bu ucbucaq duzbucaqlidir")
#     else:
#         print("Bu ucbucaq duzbucaqli deyil")

# duzbucaqlidirmi(8,10,6)





# netice_1 = canculator(1, 2, "+") 
# netice_2 = canculator(3, 4, "*") 

# print(netice_1-netice_2)

# print(type(cem_1))
# print(type(cem_2))

# print(cem_1)
# print(cem_2)



# funksiya_a("Hesen" , "Ali")
# adam_adi = input()

# funksiya_a()



# funksiya_a("Hesen")

# funksiya_a("ALi")
# funksiya_a(5)


# def ucbucagin_novunu_tap (a,b,c):
#     if a < 0 or b < 0 or c < 0:
#         return "Bele bir ucbucaq yoxdur"
    
#     if a == b == c == 60:
#         return "Beraberyanli ucbucaqdir"

#     elif a + b < c: 
#         return "Korbucaqli ucbucaqdir"
         

# ucbucagin_novunu_tap(-20, 20, 80)
# netice = ucbucagin_novunu_tap(-20, 20, 80)

# if "yoxdur" in netice:
#     print("Baki balaca seherdir")


# list_a =[10,9, 8, 7, 6, 5, 4, 3, 2, 1]
# list_a.sort()


# result = factorial(n)
# print(f"{n} faktoriali = {result}")


# def funskiya_a_c(x): 
#     cavab = x + 2
#     return cavab
    

# print(funskiya_a_c(6))
# print(funskiya_a_c(8))
# print(funskiya_a_c(20))
# print(funskiya_a_c(25))


#! Rekursiv funksiya

# n = int(input())


# def funksiya_a(t):
#     print("emeliyat yerine yetirildi")
#     funksiya_a(2)


# funksiya_a(23)


# def factorial(n):
#     if n == 0:
#         return 1
#     else: 
#         return n * factorial(n - 1)

 #return  5* factorial(4)  4* factorial(3)   3*factorial(2)  2 *factorial(1)  1* factorial(0) 1
# 5!  5 * 5-1 * 5-1-1  5-1-1-1 

# print(factorial(5))




# list_a = (2, 4 ,5 )
# print(bool(list_a))




# def f(x):
#     if x < 0:
#         return 0
#     if x > 100:
#         return 0

#     print(x)


# f(-3)
# f(105)
# f(64)


#Funksiya hər şey return edə bilər
# def f():
#     return ['foo', 'bar', 'baz', 'qux']
 

# print(f())

# print(f()[2])

# print(f()[::-1])

# dict_a= {
#     "key":"value"
# }

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


# Instagran user passowrd


# from curses import longname
# user_password = "Bakugan612"

# # login for teleqram
# def login(username, password, age) -> bool:
#     """Bu funksiya instarame giris ucundur
    
#     Args:
#         username (str): istifadecinin instagram  istifadeci adi
#         password (str): intifadecinin instagram sifresi
#         age (int): istifadecinin yasi

#     Returns:
#         bool: neticeniin true ve ya false olaraq return edir 
#         """


#     if age>18:
#         print("xos gelmisiniz")
    
    
    
#     return 23


# login("u","p", "salam")

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

# uce_vur = lambda x : 1 if x== 0 else x* uce_vur(x-1)


# def uce_vur(a):
#     return  a*3


# print(uce_vur(5))

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



# def edede_vur(n):
#   return lambda a : a * n


# k = int(input("k: "))
# edede_vur_k = edede_vur(k)


# print(edede_vur_k(3))

# def topla(a, b):
#     return a+b
# k = cem()

# print(k(2,3))

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
# Object  orianted programing
# Esya yonumlu proqramlasdirma

# class esyamizin tipi. classdan yaranan butun obyektle 
# hemin class in daxilindeki fieldlere ve methodlara  sahib olmus olur

# object - esyamizin classdan yaradiriq 

# field-properties    ---- obyektin ozelikleri
# methods -- funksiyalarimiz 

 

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




# class Human:
#     # constructor 
#     name_in_god = "Bende"
#     def __init__(self, name, lastname):
#         self.name = name
#         self.lastname = lastname
#         self.fullname = name + " " + lastname
        
        
    # def __str__(self):
    #     return  self.fullname
        
        
    # def __repr__(self):
    #     return  self.fullname + " tanrının yanında: " + self.name_in_god 
    
    

# farid_obj = Human("Farid","Habibli")
# mahammad_obj = Human("Farid","Habibli")


# print(farid_obj == mahammad_obj)
# print(mahammad_obj)

# print(farid_obj)

# print(type(farid_obj))




# class Sinif:
#     def __init__(self, x,y): 
#         self.x = x
#         self.y = y
        
#     def get_user_data(self):
        
#         print("x:",self.x)
#         print("y:",self.y)
     


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




# class Human:
#     def __init__(self,name,last,age):
#         self.name = name
#         self.last = last
#         self.age = age
        

#     def yemek_yemek(self):
#         print(f"{self.name} yemek yedi.")

#     def yas_artmaq(self):
#         self.age = self.age + 1
#         print(f"{self.name} yas artdi. yeni yas:{self.age}")


#     def __str__(self):
#         return self.name + " " + self.last


# class Hekim(Human):
#     def __init__(self,name,last, age):
#         super().__init__(name,last,age)
    


# class Muellim(Human):
#     def __init__(self,name,last, age, academic_level):
#         super().__init__(name,last,age)
#         self.academic_level = academic_level
    
#     def get_def(self,deyisgen):
#         return self.name + " " + self.last + " " + self.academic_level
   
    # Override
    # Overloading 
    
# hekim_a = Hekim("Ali","Sahib", 24)
# muellim_a = Muellim("Ali","Sahib", 24,"ProfessorDoktor")
# print(hekim_a)     
# print(muellim_a)     


