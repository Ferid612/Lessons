# dict_a = {
#    "value_1":10,
#    "value_2":20,
#    "value_3":30,
# }


# max=dict_a["value_1"]
# max_key = "value_1"
# for key in dict_a.keys():
#    if dict_a[key]>max:
#       max = dict_a[key]
#       max_key = key
      
   
# print(max)
# print(max_key)
      
   



# def f(*args):
#     for i in args:
#             print(i)


# a = [1, 2, 3]
# t = (4, 5, 6)
# s = {7, 8, 9}

# f(*a, *t, *s)
# def f(a: int, b: int) -> float:
#     print(a, b)
#     return("salam")


# f(1, "2")

# a= f(1,"34a")
# print(a)
# f.__annotations__

# book.py

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def __repr__(self):
#         class_name = type(self).__name__
#         return f"{class_name}(title={self.title!r}, author={self.author!r})"
  
#     def __str__(self):
#             return self.title

# odyssey = Book("The Odyssey", "Homer")

# print(repr(odyssey))
# print(odyssey)


# inheritance.py

class Parent:
    hair_color = "brown"

class Child(Parent):
    hair_color = "purple"
    
    
print(Parent.hair_color)