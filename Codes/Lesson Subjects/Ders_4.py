# from Codes.Lesson Subjects.Ders_4 import fakt

# from Codes.Lesson Subjects.Ders_4 import snake_case

# from Codes.Lesson Subjects.Ders_4 import snake_case

# Sual filan filan sualin izahi

# burda ikideyiskenin yerini deyisdik
# a = a+ b
# b = a- b
# a = a- b
"""_summary_
    Bu funiksiya nin meqsedi filankesdir
    Burda deyiskenler bunlardir 
    arg_1 : bu en boyuke ededi 
    arg_2 : 
    Returns:
        _type_: _description_
"""



#! Funksiyalar 

ad_1 = "Hesen"
ad_2 = "Ali"
ad_3 = "Mamed"
ad_4 = "Arif"


# print
# print(teta)
# teta("Hesen Molladi")
# print(f"Salam {ad_2}, necesen?")
# print(f"Salam {ad_3}, necesen?")
# print(f"Salam {ad_4}, necesen?")

# def snake_case(arg_1, arg_2 = " Tural"):
#     print(str(arg_1) + arg_2)



# snake_case("Salam Necesen")


# deyisgenlerin adi ve funksiyalarin pep8 snake_case  standarti ile yazilir

def say_hello(ad, prefix = "insan", ardicil_cumle = "necesen. Ne var ne yox?"):
    print(f"Salam {ad} {prefix}, {ardicil_cumle}")

    
# say_hello("Eli", "Adam")
# say_hello(ad=ad_1, prefix="bey", ardicil_cumle="necesen menim qardasim?")
# say_hello(prefix="muellim", ad=ad_2, ardicil_cumle="ders gecikirsen")
# say_hello(ad_3, "usta")


# print(f"Salam {ad_1}")

# say_hello()
# say_hello()
# say_hello()
# say_hello()
# say_hello()


# def funksiya_a(item,item_3 ,  item_2 = "Mehemmed" ,  ):
#     print(f"Salam {item}")
#     print(f"Salam {item_2}")
#     print(f"Salam {item_3}")
    
    
    
def canculator(number_1, number_2, operator):
    if operator == "+":
        return number_1 + number_2        
    
    elif operator == "-":    
        return number_1 - number_2
    
    elif operator == "*":
        return  number_1 * number_2
    
    return number_1 / number_2



# cem_1 = canculator(1, 2, "+") 

# cem_2 = canculator(3, 4, "+") 


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


def ucbucagin_novunu_tap (a,b,c):
    if a < 0 or b < 0 or c < 0:
        return "Bele bir ucbucaq yoxdur"
    
    if a == b == c == 60:
        return "Beraberyanli ucbucaqdir"

    if a + b < c: 
        return "Korbucaqli ucbucaqdir"
         

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

#! Nezrin*  We were Here
#! Rekursiv funksiya




# import time
# def funksiya_a(t):
#     print("emeliyat yerine yetirildi:",t)
#     time.sleep(1)
#     funksiya_a(2)
    

# funksiya_a(23)

# b = 5 
# fakt = 1
# for i in range(1,6):
#     fakt*=i

# print(fakt)

# 5
# def factorial(i):
#     if i==0 or i ==1: 
#         return 1
    
#     return i*factorial(i-1)  

# 5 *4* 3 * 2 *1
    
# print(factorial(5))



# def hesabla(eded_1,eded_2):
#     c = 4*eded_1 + 0.20
#     e = 5*c
#     x = 10*eded_2*e

# def ucbucagin_perimetrini_hesable(a,b,c):
#     perimeter = a +  b + c
#     return True
    
    
# netice_1 = ucbucagin_perimetrini_hesable(3,4,5)
# netice_2 = ucbucagin_perimetrini_hesable(6,7,8)
# netice_3 = ucbucagin_perimetrini_hesable(8,9,10)

# print(netice_1 + netice_2 + netice_3)

    



# hesabla(eded_1=p, eded_2=o)
# n = int(input("n: "))

# fakt = 1 
# while n!=0:
#     fakt=fakt*n
#     n=n-1

# print(fakt)

# 5! = 5 * 4! 
# 4! = 4 * 3!


# def factorial_n(number_a):
#     if number_a == 0:

#         return 1    
#     else:
#         return number_a*factorial_n(number_a-1)
    

# print(factorial_n(5))


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


def login(request):
    username = request.get("username")
    password = request.get("password")
    
    if username is None or password is None:
        return "Username or Password are required", 401
    
    

    
    
    
    
def f(x):
    if x < 0:
        return 0
    if x > 100:
        return 0

    print(x)


# f(-3)
# f(105)
# f(64)


#Funksiya hər şey return edə bilər
import os


def f():
    return ['foo', 'bar', 'baz', 'qux']
 

# x,*y, t = f()

# print(y)
 

# print(f())

# print(f()[2])

# print(f()[::-1])



# Python dict as an argument
# key word argument 
def f(*args, **kwargs):
    # print(kwargs)
    # print(type(kwargs))
    # for key, val in kwargs.items():
    #         print(key, '->', val)
    print("args: ",   args)
    print("kwargs: ", kwargs)


# argumentleri list kimi yollanilir
# dictionary key and value

# f(1,2,3,4,foo=1, bar=2, baz=3)



# Gonderilme tipi
def f(a, b, c):
    print(F'a = {a}')
    print(F'b = {b}')
    print(F'c = {c}')



def func_a(a,b,x, d=10,e=20, *args, **kwargs):
    print("Anonym")

def e(a, b, *c, **kwargs):
    print(F'a = {a}')
    print(F'b = {b}')
    print(F'c = {c}')


t = [1,2,3]
d = {'a': 'foo', 'b': 25, 'c': 'qux'}
# f(**d)

# e(2,3,4,5)



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
def concat(prefix, *args):
    
    print(f'{prefix}  {f"{prefix}".join(args)}')


concat('//', 'a', 'b', 'c')

concat('...', 'foo', 'bar', 'baz', 'qux')

# Canculyator funksiyasi yazin



#! Docstring

# Instagran user passowrd


# from curses import longname
# user_password = "Bakugan612"

# # login for teleqram

def login(username:str, password:str, age:int) -> bool:
    """Bu funksiya instarame giris ucundur
    Args:
        username (str): istifadecinin instagram  istifadeci adi
        password (str): intifadecinin instagram sifresi
        age (int): istifadecinin yasi

    Returns:
        bool: neticeniin true ve ya false olaraq return edir 
    """

    if age>18:
        print("xos gelmisiniz")
    
    return True or False


login("a","b",12)

# def foo(bar=0, baz=1):
#     """Perform a foo transformation.

#     Keyword arguments:
#     bar -- magnitude along the bar axis (default=0)
#     baz -- magnitude along the baz axis (default=1)
#     """
#     return 5 * 6
 
 
# print(foo.__doc__)   


# #! Lambda 
# def sum(eded):
#     eded = eded+10
#     return eded
    
    
# sum = lambda eded, eded_2 : eded + eded_2 
    
# print(sum(20,30))
    
    
# x = lambda a : a + 10

# def uce_vur(a):
#     return  a*3

# print(uce_vur(5))

# print(x(5))


# def factorial_n(number_a):
#     if number_a == 0:
#         return 1    
#     else:
#         return number_a*factorial_n(number_a-1)
    

# faktorial_tap = lambda x: 1 if x==0 else x * faktorial_tap(x-1)
# print(faktorial_tap(6))


# def func(a):
#     return  a + 10

# func = lambda a, y: a * y


# print(func(10,20))

# def best_func(a):
#     print(a+10000)
#     return a + 10000


# def myfunc():
#     return best_func


# x = myfunc()

# x(20)



# def edede_vur(n):
#   return lambda a : a * n


# k = int(input("k: "))
# k = 20 
# edede_vur_k = edede_vur(0.5)


# print(edede_vur_k(100))

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
#     netice = 0
#     if parametr == "+":
#         netice = eded_1 + eded_2
    
#     if parametr == "-":
#         netice = eded_1 - eded_2
      
#     if parametr == "*":
#         netice = eded_1 * eded_2
    
#     if parametr == "/":
#         netice = eded_1 / eded_2
      
#     return netice



# parametr= input('parametr: ')

# eded_1, eded_2,parametr, netice = canculator(parametr)
# print(f"{eded_1} {parametr} {eded_2}  = {netice}")


# def best():
#   print("Salam dunyani")



#! OOP 


# Object  orianted programing
# Esya yonumlu proqramlasdirma

# class esyamizin tipi. classdan yaranan butun obyektle 
# hemin class in daxilindeki field-attribute-properties ve methodlara  sahib olmus olur

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


# yas 
# ad
# soyad 


# class Human:
#     name_in_god_level = "Bende"
#     pull_migdari = 0
#     def __init__(self, name_1, lastname_1):
#         self.name = name_1
#         self.lastname =lastname_1
#         self.fullname = name_1 + " " + lastname_1
    
#     def isle(self, mebleg):
#         self.pull_migdari += mebleg
        
        
# ramiz_obj =  Human("Ramiz", "Zulfuqarov")
# farid_obj =  Human("Farid", "Habibli")
        
        
# print(farid_obj.fullname)
# print(farid_obj.pull_migdari)
# farid_obj.isle(10)
# farid_obj.isle(20)

# print(ramiz_obj.fullname)
# print(ramiz_obj.pull_migdari)
# ramiz_obj.isle(40)



# print(farid_obj.fullname)
# print(farid_obj.pull_migdari)
# print(ramiz_obj.fullname)
# print(ramiz_obj.pull_migdari)


# farid_obj = Human("Farid","Habibli")
# mahammad_obj = Human("Farid","Habibli")


# print(farid_obj == mahammad_obj)
# print(mahammad_obj)

# print(farid_obj)
# a:int = 12
# print(type(12))




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



class Human:
    def __init__(self,name,last,age):
        self.name = name
        self.last = last
        self.age = age
        

    def yemek_yemek(self):
        print(f"{self.name} yemek yedi.")

    def yas_artmaq(self):
        self.age = self.age + 1
        print(f"{self.name} yas artdi. yeni yas:{self.age}")


    def __str__(self):
        return self.name + " " + self.last
    def __repr__(self) -> str:
        return self.name + " " + self.last + " " + str(self.age)
        
   
class Hekim(Human): # inheritance # 
    def __init__(self,name,last, age):
        super().__init__(name,last,age)
        

class Muellim(Human):
    def __init__(self,name,last, age, academic_level):
        super().__init__(name,last,age)
        self.academic_level = academic_level
    

    # Override
    # Overloading 
    
    
os.system("clear")
# hekim_a = Hekim("Sebuhi","Huseynov", 24)
# muellim_a = Muellim("Turan","Dasdemirov", 24,"ProfessorDoktor")
# human = Human("Hasan","Aliyev",23)

# print(repr(human))


# print( type(hekim_a))

# print( isinstance(muellim_a,Muellim))


# def say_hello(arg):
#     print(f"Hello {arg}")
    


# Bura bizim əramizdi 


#! Destructor
# class Employee:
 
#     # Initializing
#     def __init__(self):
#         print('Employee created.')
 
#     # Deleting (Calling destructor)
#     def __del__(self):
#         print('Destructor called, Employee deleted.')
 
# obj = Employee()


class Person:
    pass

    
    
def func():
    pass

