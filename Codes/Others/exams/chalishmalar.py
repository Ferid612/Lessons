
# Listi tersine cevirin
# list_a = [3,2,4,234,-1,42,132,123,0]
# list_b = [0, 123, 132, 42, -1, 234, 4, 2, 3]


# Listi Artan sira ile duz
# list_a.reverse()
# print(list_a)
# if list_a[0] > list_a[1]:
#     list_a[0],list_a[1] = list_a[1],list_a[0]
    
# if list_a[1] > list_a[2]:
#     list_a[1],list_a[2] = list_a[2],list_a[1]
    
        
# for item in list_a:
#     a = 0
#     while a < len(list_a)-1:
#         if list_a[a] > list_a[a+1]:
#             list_a[a], list_a[a+1] = list_a[a+1], list_a[a]
#         a+=1
        
# print(list_a)


# def listi_goster(list_b):
#     for a in list_b:
#         print(a, end = " ")
    
#     print()
    
    


# list_a = [1,2,3,4,5,6,7]
# list_b = listi_goster(list_a)
# cem = sum(list_a)

# print("list_b: ", list_b)

# def tersine_cevir(str_a):
#     str_a = str_a[::-1]
    
    
# var_str = "Salam Baki"
# tersine_cevir(var_str.tersine_cevir())

# txt = var_str.upper()
# txt= txt + "Terekeme"

# print(txt)
# a = 20
# b = 30

# cem = a+b

# if cem > 40:
#     print("boyukdur")
# else:
#     print("kicikdir")    
    

# d = b = e = 25
# print("d:", d)
# print("b:", b)
# print("e:", e)


# string - str - yazi text 
# test_a = "Salam""

# integer int - tam eded 
# test_b = 20

# float ondaliq eded 
# test_c = 2.5

# print(type(test_a))
# print(type(test_b))
# print(type(test_c))

#Data tipi
# Data type

# print("5" < "10")


# string yazi tipidir. 
# integer tam ededleri yadinda saxlayir

# musteri_ad =  input("Adinizi girin: ")
# print("musteri bunu dedi:", musteri_ad)


# a = int("20")
# print(type(a))




# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def __repr__(self):
#         class_name = type(self).__name__
#         return f"{class_name}(title={self.title!r}, author={self.author!r})"

#     def __str__(self):
#         return self.title + " " + self.author

# odyssey = Book("The Odyssey", "Homer")
# print(odyssey)
# print(repr(odyssey))

# print(odyssey.author)

# print(repr(odyssey))



# class Dog:
#     species = "Canis familiaris"

#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed

#     def __str__(self):
#         return f"{self.name} is {self.age} years old"

#     def speak(self, sound):
#         return f"{self.name} says {sound}"



# class JackRussellTerrier(Dog):
#     def speak(self):
#         return f"{self.name} mew mew"

# class Dachshund(Dog):
#     def speak(self):
#         return f"{self.name} says how how"

# class Bulldog(Dog):
#     pass


# miles = JackRussellTerrier("Miles", 4, "blue cins_a")
# buddy = Dachshund("Buddy", 9 ,"cins_b")
# jack = Bulldog("Jack", 3,"cins_c")
# jim = Bulldog("Jim", 5,"blue cins")


# print(isinstance(miles, JackRussellTerrier))

# print(miles.speak())
# print(buddy.speak())
# print(jack.speak("Ta ta"))

# a = 23
# print(isinstance(a, str))

# a = 23
# for i in a:
#     print(a)



# def cem(a, b, *args):
    
#     return a + b + sum(args)


# print(cem(2,3))
# Overloading
# Polimorfizm



# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)

# print(type(myit))

# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

# print("cox onemli bir funskiya")

# def Doiterable(collection_data):
#     my_iter = iter(collection_data)
    
#     while True:
#         try:
#             print(next(my_iter))
#         except:
#             print("iterable object bitdi")
#             break        
        
        
# list_a = [10,20,30,40,50,60,70,80,90,30,40,50,60,70,80,90]
# Doiterable(list_a)











# class Kisi:
#     def __init__(self, ad):
#         self.ad = ad

# class Ogrenci(Kisi):
#     def __init__(self, ad, sinif, okul_numarasi):
#         super().__init__(ad)
#         self.sinif = sinif
#         self.okul_numarasi = okul_numarasi

# class Ogretmen(Kisi):
#     def __init__(self, ad, brans, sicil_numarasi):
#         super().__init__(ad)
#         self.brans = brans
#         self.sicil_numarasi = sicil_numarasi



# class Personel(Kisi):
    
#     def __iter__(self):
#         self.a = 1
#         return self
    
#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#           raise StopIteration
        
#     def __init__(self, ad, pozisyon, calisma_saatleri):
#         super().__init__(ad)
#         self.pozisyon = pozisyon
#         self.calisma_saatleri = calisma_saatleri


# person_a = Personel("hasan","Devops","GeceGunduz")
# myiter = iter(person_a)

# for item in myiter:
#     print(item)

# int_a = [22.2]

# print("a">2)
# print(int_a.__class__.__class__)
  
# try:

#     print(10/0)
#     a = 10 / 0
# except:
#     print("error bas verdi")

# print("cox onemli funksiya")


# def myfuncC():
#     print(x)

# def myfunc():
#   print("funksiyanin daxili: ", x)

# myfunc()


# x = 30

# print("sonra: ",x)




# verilen_cumleler=  """
# # Listlər
# 1. Siyahı yaradın və bu siyahının elementlərini tərsinə çevirin.
# 2. Siyahı yaradın və bu siyahıya elementlərin cəmi hesablayın. sum() funksiyasını işlətməyin.
# 3. Siyahı yaradın və bu siyahıdakı elementləri kiçikdən böyüyə və ya böyüyün kiçiyinə sıralayın. İki üsulla yazın. Həm hazır list funksiyasından istifadə edərək. Həm etməyərək.
# 4. Verilmiş siyahıdakı bütün dublikat elementləri silmək üçün proqram yazın.
# 5. İki siyahı yaradın və bu iki siyahının kəsişməsini (ümumi elementlərini) tapan proqram yazın.
# 6. Siyahıdakı elementlərin ədədi ortasını və medianını hesablayan proqram yazın.
# 7. Siyahı yaradın və bu siyahıdakı elementləri elementin sayına görə çeşidləyən proqram yazın.  (Yəni, ən çox təkrarlanan elementdən ən az təkrarlanan elementə doğru)
# 8. Siyahıdakı bütün sadə ədədləri tapan proqram yazın.
# """

# input_str = input()


# sozler = verilen_cumleler.split(input_str)
# print(len(sozler))
# print(sozler)







