
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



class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"



class JackRussellTerrier(Dog):
    def speak(self):
        return f"{self.name} mew mew"

class Dachshund(Dog):
    def speak(self):
        return f"{self.name} says how how"

class Bulldog(Dog):
    pass


miles = JackRussellTerrier("Miles", 4, "blue cins_a")
buddy = Dachshund("Buddy", 9 ,"cins_b")
jack = Bulldog("Jack", 3,"cins_c")
jim = Bulldog("Jim", 5,"blue cins")


print(miles.speak())
print(buddy.speak())