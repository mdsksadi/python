
'''
There are various operators in python.
--Arithmetic Operators
--Assignment Operators
--Relational Operators
--Logical Operators
--Unary Operators

'''
#Arithmetic Operators
'''
There are some "Arithmetic Operators" in Python.
--Addition ==> "+"
--Subtraction ==> "-"
--Multiplication ==> "*"
--Division ==> "/"
--Modulus ==> "%"
--Exponentiation ==> "**"
--Floor division ==> "//"

'''
x=2
y=3

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)          #It shows the "Reminder" of the division
print(x**y)         #It shows the exponential like "x^y"
print(x//y)         #It first devide and then make the result "floor"
'''
import math

z=math.floor(y/x)   #We can also doing "floor" operation like this. We can also find the "ceilling" by using "math.ceil()" function
print(z)
'''

#Assignment Operator

'''
When I use equal symbol (=) that is assignment operator

'''
a=8
b=8
a=a+2
print(a)

b +=2           #It means "b=b+2"
print(b)

a -=2           #It means "b=b-2"
print(a)

a *=3           #It means "b=b*2"
print(a)

a /=2           #It means "b=b/2"
print(a)

c,d=5,6         #We can also assing multiple values at the same time.
print(c)
print(d)

#Unary Operators

n=7
print(n)        
n=-n            #We just inverst the value of "n" by using "Unary Operator"
print(n)


#Relational Operators

print(a>b)
print(a<b)
print(a==b)
print(a<=b)
print(a>=b)
print(a!=b)

#Logical Operators
'''
There are 3 "Logical Operators"
--And
    For "And", all the conditions must fulfill
--Or
    For "Or" only one candition fulfill is okay
--Not
    For "Not", we will get a reverse output

'''

a=5
b=4
print(a<8 and b<5)      #It's "True" because both conditions are satisfied
print(a<8 and b<2)      #It's "False" because only one conditon is satisfied

print(a<8 or b<5)       #It's "Ture" because both conditions are satisfied
print(a<8 or b<2)       #It's "True" because one condition is satisfied

x=True
print(x)            #The result is "True" 
print(not x)        #The result is "False" because we put not at the fron of x. So it reverse the value.
print(x)            #The result is "True" because it shows the previous value
x=not x             #Now it changes the value
print(x)            #Now the value of "x" is "False"



