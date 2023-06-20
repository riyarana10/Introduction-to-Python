# # if else if and else statment
if True:
    print('its true')

if 3>2:
    print("true")
else:
    print("false")


x = 'bank'

if x == 'not bank':
    print("cool")
elif x == 'hello':
    print("hello")
else:
    print("bank")


# for loop
mylist = [1,2,3,4,5,6,7,8,9,10]

for i in mylist:
    print(i)
    
# check for even
for i in mylist:
    if i%2 == 0:
        print(f'even : {i}')
    else: 
        print(f'odd : {i}')
        

mylist = [(1,2,3),(4,5,6),(7,8,9)]
for i in mylist:
    print(i)


for a,b,c in mylist:
    print(c)



# while loop
x = 0
while x<5:
    print(f'{x} is less than 5')
    x +=1
else:
    print("x is not less than 5")

# break continue and pass in loop

for i in "hello":
    # comment
    pass




    