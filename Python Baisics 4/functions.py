# function creation
def my_function():
  print("Hello from a function")

# function calling
my_function()


# function arguments and parameters
def my_function(fname):
  print("Hello "+fname)

my_function("Emil")
my_function("Tobias")
my_function("Linus") 


# multiple parameters
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("riya", "rana") 


# Arbitrary Arguments, *args

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus") 



# **kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes") 



# default arguments
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil") 


#  passing a list as an argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)



# return value

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9)) 




