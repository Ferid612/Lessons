
# temp = my_list[0]
# my_list[0] = my_list[-1]
# my_list[-1] = temp


# temp = my_list[1]
# my_list[1] = my_list[-2]
# my_list[-2] = temp



# my_list = [1,2,3,4,5,6,7,8,9]
# for i in range(len(my_list)//2):
#     temp = my_list[i]
#     my_list[i] = my_list[-1-i]
#     my_list[-1-i] = temp


# print(my_list)

# # for j in range(len(mylist) ):

#     for i in range(  len(mylist) -1  ):
#         if mylist [i] > mylist [i+1]:
#             temp=mylist [i]
#             mylist [i]=mylist [i+1]
#             mylist [i+1]=temp

# print(mylist)

# 1. Siyahı yaradın və bu siyahının elementlərini tərsinə çevirin.

# 2. Siyahı yaradın və bu siyahıya elementlərin cəmi hesablayın. sum() funksiyasını işlətməyin.

# 3. Siyahı yaradın və bu siyahıdakı elementləri kiçikdən böyüyə və ya böyüyün kiçiyinə sıralayın. İki üsulla yazın. Həm hazır list funksiyasından istifadə edərək. Həm etməyərək.

# 4. Verilmiş siyahıdakı bütün dublikat elementləri silmək üçün proqram yazın.

# 5. İki siyahı yaradın və bu iki siyahının kəsişməsini (ümumi elementlərini) tapan proqram yazın.

# 6. Siyahıdakı elementlərin ədədi ortasını və medianını hesablayan proqram yazın.

# 7. Siyahı yaradın və bu siyahıdakı elementləri elementin sayına görə çeşidləyən proqram yazın.  (Yəni, ən çox təkrarlanan elementdən ən az təkrarlanan elementə doğru)

# 8. Siyahıdakı bütün sadə ədədləri tapan proqram yazın.


# number_a = 20
# number_b = 30


# temp = number_a
# number_a = number_b
# number_b = temp


# number_a =  number_a + number_b
# number_b = number_a - number_b
# number_a = number_a - number_b
# print(number_a)
# print(number_b)


# siyahi_a =siyahi_a[::-1]
# print(siyahi_a)


# siyahi_a = [0,1,2,3,4,5,6,7,8,9]

# for index in range(len(siyahi_a)):
#     temp = siyahi_a[index]
#     siyahi_a[index] = siyahi_a[-1 - index]
#     siyahi_a[-1 -index] = temp 
    

# print(siyahi_a)


# temp = siyahi_a[0]
# siyahi_a[0] = siyahi_a[-1]
# siyahi_a[-1] = temp


# temp = siyahi_a[1]
# siyahi_a[1] = siyahi_a[-2]
# siyahi_a[-2] = temp




# siyahi_a[1] = siyahi_a[-2]
# siyahi_a[2] = siyahi_a[-3]
# siyahi_a[3] = siyahi_a[-4]
# siyahi_a[4] = siyahi_a[-5]
# siyahi_a[5] = siyahi_a[-6]
# siyahi_a[6] = siyahi_a[-7]
# siyahi_a[7] = siyahi_a[-8]

# print(siyahi_a)


# list_a = [2,7,35,43,5,6,8]

# for a in list_a:  
#   for i in range(len(list_a)- 1):
#     if list_a[i]<list_a[i+1]:  
#       temp = list_a[i]
#       list_a[i] = list_a[i+1]
#       list_a[i+1] = temp
  

# print(list_a)



#!Strings Methods

#! Strings

# Multiline Strings

# string_a = """Salam baki necesen.
# Neynirsen?
# Halin ehvalin."""
# print(string_a)
# print(type(string_a))

# for herf in "SalamBaki":
#     print(herf)


#! indexing in string
# var_a = "Dunya senin"
# herf = var_a[::-1]
# print(herf)
# print(len(var_a))


#! in keyword in strings


txt = "The best things in life are Free!"
# new_txt = txt.

# print(new_txt)
# list_a = ["Farid", "Mahammad","Muhammad","Nicat"]


# new_text = ",".join(list_a)

# print(new_text)

# print(txt.find("in",12))

# print(txt.upper().count("F"))


#*upper
#*lower
#*split
#*strip
#*format

#*startswith
#*endswith
#*count

#*find
#*join
#*repleca



#*encode
# string1 = 'I am Job-Reådy'

# print ( string1.encode( encoding = "ascii", errors = "namereplace" ) )
# print ( string1.encode( encoding = "ascii", errors = "replace" ) )
# print ( string1.encode( encoding = "ascii", errors = "ignore" ) )




#*endswith

# soz_1 = "Crio Dev Community."

# result = soz_1.startswith('Dev',5,7)
# print(result)



# result = soz_1.endswith('Dev', 0, 8)
# print(result)

# result = string1.endswith('Crio Dev', 0,8)
# print(result)


#* find
# var_string = "Salam Baki, Bu gun hava guneslidir Baki."
# print(var_string[::-1])


# print(var_string[35:])



# result_find = var_string.find("Baki",10,20)
# # /
# print(result_find)



# var_string = "Baki Necesen Baki Bize Baki Lazimdi"
#*calisma: İlk Necesen sozunden sonra gelen ilk sozu tap



#*Join

# myDict = {"Company": "Crio", "Designation": "Developer"}
# myList = [ 'Revive', 'Your', 'Dev', 'Career' ]


# variable_a = "--".join(myList)
# variable_a += "TEST2"

# print(variable_a)


#* Partitions
# myStr = 'Personalised Career Guidance Salreeram '
# myValue = 'reer'
# res = myStr.partition(myValue)

# print(res)

# file_path = '/home/faridh/Desktop/Lessons/suallar.txt'
# with open(file_path, 'r') as f:
#   print(f)
  
  
#*Repleca
# myStr = 'Crio focuses on project-based learning. Crio encourages learn by doing'
# old_value = 'Crio'
# new_value = 'TEST612'

# print(myStr)
# res = myStr.replace(old_value, new_value)
# print(res)

# list_a = {"Salam","Neceseb","Hello"}

# print(list_a[0])
# print(list_a)


#! TUPLE

# thislist = ["apple", "banana", "cherry", "cherry"]
# thistuple = ("apple", "banana", "cherry", "cherry")

# list_a = [0]

# print(list_a)
# print(type(list_a))

# thislist[0] = "Lemon"
# print(thislist[0])
# print(thislist)

# thistuple[0] = "KIWI"
# print(thistuple[0])



# Dublicate
# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple)
#
# Len tupple

# thistuple = ("apple", "banana", "cherry","Test")
# print(len(thistuple))

# verilen_string = "Salam frontend , backend , Broend 
# , locked"
# Some tuples

# tuple1 = ("apple", "banana", "cherry")
# tuple2 = (1, 5, 7, 9, 3)
# tuple3 = (True, False, False)
# tuple1 = ("abc", 34, True, 40, "male")

#Access
# thistuple = ("apple", "banana", "cherry", "cherry", "cherry")
# print(thistuple[1])
# print(thistuple[-1])
# print(thistuple[2:5])


#! Update Tupple


# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
# print(x)



# Add items
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)






#* Append method to tuple

# tupla_a.append("orange")

# tupla_a = ("apple", "banana", "cherry")
# y = ("orange",)

# print(y)
# print(type(y))


# tupla_a = tupla_a + y




# print(tupla_a)


#Remove
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")

# thistuple = tuple(y)
# print(thistuple)




# list_a = [1,2,3,3,4,5,5,7,7,9]
# b, *c  = list_a



# print("a:",a)
# print("b:",b)
# print("c:",c)


#! Using Asterisk*

# list_a = (2, 4, 6)
# a,b,c = list_a

# print(a)
# print(b)
# print(c)



# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# green, yellow, *red = fruits


# print(green)
# print(yellow)
# print(red)




#! SET
# myset = {"apple", "banana", "cherry","apple", "banana"}

# print(myset)

# print(type(myset))
# print(myset)
# # str.upper()

# thisset = {"apple", "banana", "cherry", "apple"}
# print(thisset)

#! Attention 1  and True

# thisset = {"apple", "banana", "cherry",  True,1, 0, 2}
# print(thisset)



#* Access set items
# Indekslerle elementlerine muraciet etmek olmur
# Deyismek olmur


# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)


# thisset.pop()
# thisset.pop()

# print("thisset:", thisset)

# print(thisset)
# var = thisset.pop()
# var_b = thisset.pop()
# print(var)
# print(var_b)
# print(thisset)



# #* Add items

# thisset = {"apple", "banana", "cherry"}
# thisset.add("orange")
# print(thisset)




# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya","cherry"}
# # Or

# mylist = ["kiwi", "orange","banana"]
# thisset.update(mylist)
# print(thisset)



#*Remove

# thisset = {"apple", "banana", "cherry"}
# thisset.remove("banana")
# thisset.remove("banana")

# print(thisset)

# #or
# thisset.discard("banana")
# thisset.discard("banana")
# thisset.discard("banana")
# var_b = thisset.discard("banana")

# print(var_a)
# print(var_b)
# print(thisset)



# Random choice
# thisset = {"apple", "banana", "cherry"}
# x = thisset.pop()
# print(x) #removed item
# print(thisset) #the set after removal



#* Join

# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3,'a'}
# set3 = set1.union(set2)
# print(set3)



#* Intersection
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.intersection_update(y)
# print(x)

# print(result_a)


# result = x.intersection_update(y)
# print(result_a)

# print( x)
# print( result)



# simmetric ferq
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}


# x =  x - y + (y - x)

# x.symmetric_difference_update(y)

# result = x.symmetric_difference(y)
# print(x)
# print(result)


# Alt coxlugugurmu

# x = {"a", "b", "c"}
# y = {"f", "e", "d","a", "c", "b"}

# z = y.issuperset(x)
# print(z)




# x = {"f", "e", "d","a", "c", "b"}
# y = {"a", "b", "c"}

# test_str =  "-".join(x) 
# test_str = test_str.split(" ")
# print(test_str)




# x.union(y)

# for a in y:
#    x.add(a)

# print(x)


# set_a = {1,2,3,4,5,6,7,8,9,10}
# print(type(set_a))
# for a in set_a:
#   print(a)

# list_a = [1,1,1,1,2,2,3,2,2,1]
# list_a = list(set(list_a))
# print(list_a)


#! DICT
#

# car = {"brand": "Ford", "model": "S-class", "year": 2012}

# english_levels = {
#     "a1":"beginner",
#     "a2":"elemetry",
#     "c1":"pre-intermadate",
#     "b1":"pre-intermadate12",
# }



# matris = [[1,2,3],[2,3,4],[7,8,9]]

# print(matris[0][2])


# for list_a in matris:  
#   for item in list_a:
#     print(item, end=' ')

#   print()


# print("Salam")
# print("Hesen")

#*Duplicates
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(thisdict)

# print(    thisdict["brand"]        )




# Attension


# matris_a = [[0,1,21],[2,3,4],[5,6,7],[8,9,10]]


# print  (  matris_a[2][2]    )

# print(           matrix_a[1][2]         )


# thisdict = {

#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue",23],
#  }


# print(  thisdict["colors"]  )


# # Get method

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "oil_version": "dizel",
#   "year": 2020
# }

# # x = thisdict["oil_version"]
# x = thisdict.get("oil_version","benzin")

# print(x)

# print(x)



# print(x)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }


# print(thisdict.items())

# for key,value in thisdict.items():  
#   print("key:",key,"value:", value)

# list_adam_adlari = ["Hasan","Ali"]

# for index,item in enumerate(list_adam_adlari):
#   print(index,item)
  
  
  
# dict_2  = thisdict.copy()

# dict_2["brand"] = "BMW"

# print(dict_2)
# print(thisdict)




  # print(f"key= {key}")
  # print(f"value= {value}")

# Keys ATTENTION

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.keys()

# print(x) #before the change

# car["color"] = "white"

# print(x) #after the change



# VALUES ATTENTION
# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.values()

# print(x) #before the change

# car["year"] = 2020

# print(x) #after the change


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# dist_2 = thisdict.copy()

# dist_2["brand"] ="BMW"

# print(dist_2)
# print(thisdict)



# UPDATE
# thisdict = {
#   True : "Ford",
#   12 : "Mustang",

# }
# thisdict.update(
#   {
#     "year": 2020,
#    "model":"BMW",
#    "oil_type":"benzin"
#    }
#   )


# thisdict[True] = 23

# print(thisdict)


# #REMOVE

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)
# print(thisdict.popitem())


# print(thisdict)
# 
# thisdict.pop("model")
# print(thisdict.pop("model"))
# print(thisdict)

# print(thisdict)


#!FOR WITH DICT

# for x in thisdict:
#   print(x)

# for x in thisdict:
#   print(thisdict[x])


# for x in thisdict.values():
#   print(x)


# for x in thisdict.keys():
#   print(x)




# For above nested dicts
# list_a = [1,2,3,4,5,6,7,8,9]
# matrix_a = [1,2,3],[4,5,6],[7,8,9]


# # print(len(list_a))
# for item in matrix_a:
#   for a in item:
#     print(a, end =' ')

#   print()




# NESTED ITEMS
# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }

# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }

# child3 = {
#   "name" : "Linus",
#   "year" : 2011,
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }

# print(child2['name'])


# x = ('key1', 'key2', 'key3')

# thisdict{
#   ke
# }

# a = 20
# b = 30

# a = b

# list_a = ["SAlam","necesen",3,4]

# for index,a in enumerate(list_a):
#   print("index: ",index)
#   print("value: ",a)

# temp = a
# a = b
# b= temp

# print(a)
# print(b)


# Mediani tapma proqrami
# list_str = input("Listi daxil edin")
# list_str = input("Listi daxil edin: ")
# list_a = list_str.split(" ")

# list_a = [int(item) for item in list_a]

# list_a =[9, 8 , 7, 6, 5, 4, 3, 2, 1,0]
# list_a.sort()

# median = None
# if len(list_a)%2 != 0:
#     ortadaki_index = len(list_a) // 2
#     median = list_a[ortadaki_index]
# else:
#   ortadaki_index = len(list_a) // 2
#   median = (list_a[ortadaki_index] + list_a[ortadaki_index + 1])/2
  
  
# print(median)



# Sade olub olmadigini yoxlamaq
# list_a = [1,2,3,4,5,6,7,8,9,10,11,12]

# for eded in list_a:
#   bolunurmu = False
  
#   for i in range(2, int(eded**0.5)+1):
#       if eded % i == 0:
#         bolunurmu = True
#         break
  
        
#   if bolunurmu:
#     print(f"{eded} ededi murekkeb ededdir")

#   else:
#     print(f"{eded} ededi sade ededdir")




# Sorting
# for index in range(0, len(list_a) -1):
#     if list_a[index] > list_a[index + 1]:
#       temp = list_a[index]
#       list_a[index] = list_a[index + 1]
#       list_a[index + 1] = temp
      
      
  
