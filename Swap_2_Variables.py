
from abc import abstractclassmethod


a=5
b=6

'''
a=b
b=a
print(a)            #The result is a=6
print(b)            #The result is b=6

It will not work. So we need to find another way
'''
'''
temp=a
a=b
b=temp

print(a)
print(b)

Now it's working. But we do not want to do like this. Because here we need to use an extra variable.temp=a
a=b
b=temp

print(a)
print(b)

Now it's working. But we do not want to do like this. Because here we need to use an extra variable.

'''
'''
a=a+b       #11
b=a-b       #5
a=a-b       #6

print(a)
print(b)

It's also working. It does not matter from where I got that fomula.
But here I am using one extra bit for "11". So I will not use this formula also 

'''
#Python has a simple way to do the swap

a,b=b,a
print(a)        #The result is a=6
print(b)        #The result is b=5

