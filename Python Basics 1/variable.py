myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# variable assignment
# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)
# print('\n')
# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)
# print('\n')
# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)


# output variables
# x = "Python is awesome"
# print(x)

# x = "Python"
# y = "is"
# z = "awesome"
# print(x, y, z)

# x = "Python "
# y = "is "
# z = "awesome"
# print(x + y + z)

# global variables

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()



x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)