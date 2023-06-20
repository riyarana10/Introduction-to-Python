# Built in data types

# 1) Number data type 
x = 5
y = 10.5

print(type(x))
print(type(y))

# 2) String data type

s = "helloWorld"
print(s)
print(type(s))
print(len(s))

print(s[1])
print(s[0])

print(s[1:]) 
# it will start printing from index 1 to end

print(s[:3])
# it will start priting from start to index 2 (stop index is not included)

print(s[3:6])
print(s[::])
print(s[2:7:2])

# string concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# string format

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# escape character
txt = "We are the so-called \"Vikings\" from the north."
print(txt)



# Boolean data type
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
  
#   list data type
mylist = [1,2,3]
print(mylist)
mylist = ["hello","world","bye"]
print(mylist)
mylist = [1,"hello"]
print(mylist)


# list slicing
print(mylist[1:])
print(mylist[0:2])
print(mylist[::2])

# concatenation of list
list1 = ["my","name","is","riya"]

new_list = mylist + list1
print(new_list)


  