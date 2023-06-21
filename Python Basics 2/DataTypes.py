# # Built in data types

# # ******************************************** Number data type *******************************
# x = 5
# y = 10.5

# print(type(x))
# print(type(y))

# # **********************************String data type*****************************************

# s = "helloWorld"
# print(s)
# print(type(s))
# print(len(s))

# print(s[1])
# print(s[0])

# print(s[1:]) 
# # it will start printing from index 1 to end

# print(s[:3])
# # it will start priting from start to index 2 (stop index is not included)

# print(s[3:6])
# print(s[::])
# print(s[2:7:2])

# # string concatenation
# a = "Hello"
# b = "World"
# c = a + b
# print(c)

# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)

# # string format

# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age))


# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))

# # You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price))

# # escape character
# txt = "We are the so-called \"Vikings\" from the north."
# print(txt)



# *******************************************Boolean data type******************************************
# print(10 > 9)
# print(10 == 9)
# print(10 < 9)

# a = 200
# b = 33

# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")
  
  
#   ***************************************list data type*************************************************
# mylist = [1,2,3]
# print(type(mylist))
# print(mylist)
# mylist = ["hello","world","bye"]
# print(mylist)
# mylist = [1,"hello"]
# print(mylist)


# list slicing
# print(mylist[1:])
# print(mylist[0:2])
# print(mylist[::2])

# concatenation of list
# list1 = ["my","name","is","riya"]

# new_list = mylist + list1
# print(new_list)

# List Methods

# 1) append method
# currencies = ['Dollar', 'Euro', 'Pound']
# currencies.append('Yen')
# print(currencies)

# animals = ['cat', 'dog', 'rabbit']
# wild_animals = ['tiger', 'fox']
# animals.append(wild_animals)
# print('Updated animals list: ', animals)

# 2) clear method
# My_List = [1,2,3,4,5,6,7]
# print(My_List)
# My_List.clear()
# print(My_List)

# Sort Method
# prime_numbers = [11, 3, 7, 5, 2]
# prime_numbers.sort()
# print(prime_numbers)

#copy method
# prime_numbers = [2, 3, 5]
# numbers = prime_numbers.copy()
# print('Copied List:', numbers)

# insert method
# vowel = ['a', 'e', 'i', 'u']
# # 'o' is inserted at index 3 (4th position)
# vowel.insert(3, 'o')
# print('List:', vowel)


# List Unpacking
# colors = ['red', 'blue', 'green']
# red = colors[0]
# blue = colors[1]
# green = colors[2]

# print(red, blue, green)

# r , b, g = colors
# print(r,b,g)


# *******************************************************None*******************************************
# x = None

# if x:
#   print("Do you think None is True?")
# elif x is False:
#   print ("Do you think None is False?")
# else:
#   print("None is not True, or False, None is just None...") 
  


# **********************************************Dictionary data type******************************************
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color":"red"
}

# print(type(thisdict))
# print(thisdict)

# access item
# print(thisdict["brand"])

# x = thisdict["model"]
# print(x)
# x = thisdict.get("model")
# print(x)
# x = thisdict.keys()
# print(x)
# y = thisdict.values()
# print(y)

# update item
# thisdict["year"] = 2018
# print(thisdict["year"])


# thisdict.update({"year": 2020}) 
# print(thisdict["year"])


# adding items
# thisdict["color"] = "red"
# print(thisdict)

# thisdict.update({"color": "green"}) 
# print(thisdict)


# remove item
# thisdict.pop("model")
# print(thisdict)

# thisdict.popitem()
# print(thisdict)

# del thisdict["brand"]
# print(thisdict)

# thisdict.clear()
# print(thisdict)

# Loops in dictionary


# for x in thisdict:
#   print(x) 
# print('\n')
  
# for x in thisdict:
#   print(thisdict[x]) 
# print('\n')

# for x in thisdict.values():
#   print(x) 
# print('\n')  
  
# for x in thisdict.keys():
#   print(x)
# print('\n') 

# for x, y in thisdict.items():
#   print(x, y) 
# print('\n')  

# nested dictionary
# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# } 

# print(myfamily)
# print([myfamily["child1"]["name"]])



# *******************************************************Tuples data type*********************************************
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple)

# print(thistuple[1])
# print(thistuple[-1])
# print(thistuple[2:])

# thistuple = ("apple", "banana", "cherry")
# if "apple" in thistuple:
#   print("Yes, 'apple' is in the fruits tuple") 

# unpack tuple
# fruits = ("apple", "banana", "cherry")
# (green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)


# loop tuple
# for x in thistuple:
#   print(x) 

# join tuple 
# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3)
  
  
  
# *********************************************************sets data type*******************************************************
thisset = {"apple", "banana", "cherry"}
print(thisset)
print(len(thisset))
print(type(thisset))

thisset = set(("apple", "banana", "cherry"))
print(thisset) 

# access item
for x in thisset:
  print(x) 

# add item
thisset.add("orange")
print(thisset) 

tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset) 

# remove item
thisset.remove("banana")
print(thisset)

thisset.discard("banana")
print(thisset)

x = thisset.pop()
print(x)
print(thisset) 

thisset.clear()
print(thisset)

# thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset) 

# join sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)