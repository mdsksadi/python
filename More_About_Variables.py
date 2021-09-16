
'''
Every variable has an address.

'''

num=5
print("Address of num is:", id(num))          #We get an address "1589004036528"

name= "Sadi"
print("Address of name is:", id(name))         #Now we get different address "1589009998896"

a=10                    #Assign a value in a
b=a                     #Here let say, a and b is same

print(a)                #Show the value of "a"
print(b)                #Show the value of "b"

print("Address of a is:", id(a))            #Show the address of "a" and it is "1589004036688"
print("Address of b is:", id(b))            #Show the address of "b" and it is "1589004036688". 
#Both address are same. Because here both "a" and "b" are using same address.
#That's why python is memory efficient.

print("Address of 10 is:", id(10))           #Address of "10" is also same and that is "1589004036688"
#So address is not based on variable name. It is based on the box itself.

k=10
print("Address of k is:", id(k))            #The address of "k" is also "1589004036688". Because it is using the same box.

a=9
print("Address of a is:", id(a))            #Now the address of "a" is changed that is "1589004036656". Becaue we assign a new value inside the "a"
print("Address of b is:", id(b))            #Address of "b" is still "1589004036688". Because "b" is still refering the value "10"

k=a
print("Address of k is:", id(k))            #Now the address of "k" is "1589004036656"

'''
In pyhon we can not assign any constant. Because we can change any value at any time.
Yes we can say that, hey this is a constant. But actually we can change the value of that at any time. 
'''