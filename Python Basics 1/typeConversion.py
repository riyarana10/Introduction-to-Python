# implicit type conversion

x = 10
  
print("x is of type:",type(x))
  
y = 10.6
print("y is of type:",type(y))
  
z = x + y
  
print(z)
print("z is of type:",type(z))


# explicit type conversion
s = "10010"
  
# printing string converting to int base 2
c = int(s,2)
print ("After converting to integer base 2 : ", end="")
print (c)
  
# printing string converting to float
e = float(s)
print ("After converting to float : ", end="")
print (e)

