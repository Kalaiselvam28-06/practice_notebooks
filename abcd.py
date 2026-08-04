'''
#Right triangle
n = 5
for i in range(1, n+1):
    for j in range(i):
        print("*", end ="")
    print()
for i in range(n-1,0,-1):
    for j in range(i):
         print("*", end ="")
    print()  


n=5
for i in range(n,0,-1):
    for j in range(n-i):
         print(" ", end ="")
    for k in range(i):
        print("*",end="")
    print()

#Hollow rectangle
rows=5
cols=7
for i in range(rows):
    for j in range(cols):
        if i==0 or i==rows-1 or j==0 or j==cols-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()

#Right aligned reverse numbers
n=5
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i,0,-1):
        print(k,end="")
    print()


def my_function():
    print("Hello from a function")
my_function()

def fahrenheit_to_celsius(fahrenheit):
    return(fahrenheit-32) * 5/9
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))


def get_greeting():
    return "Hello from a function"
# message = get_greeting()
# print(message)
print(get_greeting())'''

def my_function():
    pass

#Arguments
def my_function(name):
    print(name + " Peter")
my_function("Robin")
my_function("Kevin")
my_function("Richard")
