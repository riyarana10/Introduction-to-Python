a = 200
b = 33
c = 500

# and
if a > b and c > a:
  print("Both conditions are True")
  
  
# or
if a > b or a > c:
  print("At least one of the conditions is True")
  
# not
  
if not a > b:
  print("a is NOT greater than b")
  
  

# nested if
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.") 
    

# pass statement
if b > a:
  pass