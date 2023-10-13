#! Start from here
#*Count
# list_a = ["salam", "necesen", "neynirsen", "netersen","salam"]
# var_string = "Salam Baki Necesen Baki Bize Baki Lazimdi"


# print(var_string.count("Baki"))
# print(list_a.count("salam"))


#*encode
# string1 = 'I am Job-Reådy' 
# print ( string1.encode( encoding = "ascii", errors = "namereplace" ) )
# print ( string1.encode( encoding = "ascii", errors = "replace" ) ) 
# print ( string1.encode( encoding = "ascii", errors = "ignore" ) )

#*endswith
# string1 = "Crio Dev Community." 
# result = string1.endswith('ity.', 5) 
# print(result) 

# result = string1.endswith('Dev', 4, 8) 
# print(result) 

# result = string1.endswith('Crio Dev', 0,8) 
# print(result)


#* find  
# var_string = "Baki Necesen Baki Bize Baki Lazimdi"
# result_find = var_string.find("Baki",2)
# print(result_find)


#*calisma: İlk Baki sozunden sonra gelen ilk sozu tap


#*Join
# myDict = {"Company": "Crio", "Designation": "Developer"}
# myList = [ 'Revive', 'Your', 'Dev', 'Career' ] 
# mySeparator = '#' 
# res = mySeparator.join(myList) 
# print(res)


#* Partitions
# myStr = 'Personalised Career Guidance'
# myValue = 'reer'
# res = myStr.partition(myValue) 
# print(res)



#*Replaca
# myStr = 'Crio focuses on project-based learning. Crio encourages learn by doing'
# old_value = 'Crio'
# new_value = 'Crio.Do'
# res = myStr.replace(old_value, new_value)
# print(res)




#! TUPLE 

# thistuple = ("apple", "banana", "cherry")
# print(thistuple)

# Dublicate
# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple)

# Len tupple
# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))


# Some tuples
# tuple1 = ("apple", "banana", "cherry")
# tuple2 = (1, 5, 7, 9, 3)
# tuple3 = (True, False, False)
# tuple1 = ("abc", 34, True, 40, "male")

#Access
# thistuple = ("apple", "banana", "cherry")
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
# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)


#Remove
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)

# print(thistuple)




#! Using Asterisk*

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, yellow, *red) = fruits
# print(green)
# print(yellow)
# print(red)




#! SET
# myset = {"apple", "banana", "cherry"}

# thisset = {"apple", "banana", "cherry", "apple"}
# print(thisset)

#! Attention 1  and True
# thisset = {"apple", "banana", "cherry", True, 1, 2}
# print(thisset)



#* Access set items
# Indekslerle elementlerine muraciet etmek olmur
# Deyismek olmur 

# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)



#* Add items

# thisset = {"apple", "banana", "cherry"}
# thisset.add("orange")
# print(thisset)


# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
# Or
# mylist = ["kiwi", "orange"]
# thisset.update(tropical)
# print(thisset)



#*Remove

# thisset = {"apple", "banana", "cherry"}
# thisset.remove("banana")
#or 
# thisset.discard("banana")
# print(thisset)

# Random choice
# thisset = {"apple", "banana", "cherry"}
# x = thisset.pop()
# print(x) #removed item
# print(thisset) #the set after removal


#* Join
# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
# set3 = set.union(set2)
# print(set3)


#* Intersection 
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.intersection_update(y)
# x.intersection(y)
# print(x)


# simmetric ferq 
# x =  x - y + (y - x)
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.symmetric_difference_update(y)
# x.symmetric_difference(y)
# print(x)


# Alt coxlugugurmu
# x = {"a", "b", "c"}
# y = {"f", "e", "d", "c", "b"}
# z = x.issubset(y)
# print(z)


# x = {"f", "e", "d", "c", "b", "a"}
# y = {"a", "b", "c"}
# z = x.issuperset(y)
# print(z)


#! DICT
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["brand"])

#*Duplicates
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(thisdict)


#Attension
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# Get method
x = thisdict.get("brand")
print(x)


# Keys ATTENTION
# x = thisdict.keys()

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


# UPDATE
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020,"model":"BMW"})

# print(thisdict)


#REMOVE 
# print(thisdict.pop("model"))
# print(thisdict.popitem())
# del thisdict["model"]
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


#NESTED ITEMS 
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
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }
# print(myfamily["child2"]["name"])



# x = ('key1', 'key2', 'key3')

# thisdict = dict.fromkeys(x)

# print(thisdict)