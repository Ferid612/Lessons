from math import sqrt
from Ders_4 import say_hello


print(sqrt(81))

# class Dog:
#     species = "Canis familiaris"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __repr__(self):
#         return self.name + ": " + str(self.age)
        
        
#     def __str__(self):
#         return self.name + ": " + str(self.age)

# #Constructor - init

# a = Dog("Bruno",3)
# b = Dog("Toplan",2)

# print(a)
# print(repr(a))





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



# class GermanWolf(Dog):
#     def __init__(self, name, age, breed):
#         super().__init__(name, age, breed)
    
#     pass


# german_dog = GermanWolf("German",23,"Home")

# print(german_dog.species)
# print(german_dog.name)
# print(german_dog.age)



file_text = open("Codes/data.txt","r")

a = file_text.read()
list_a = []
for item in a.split(","):
    if int(item)%2 == 0:
        list_a.append(int(item))
    
file_text_2 = open("Codes/netice.txt","w")

for item in list_a:
    file_text_2.write(str(item)+",")



# f = open("suallar_copy.txt", "r")
# print(f.read())  # returns the entire contents of a file as one string


# for a in f:
#     print(a)
# f.write("pineapples")
# f.write("kiwis")

# for a in f:   
#     print(a,end="")

# f.close()