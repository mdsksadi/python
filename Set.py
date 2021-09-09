
'''
These all are data structure:
01. list
02. dictionary
03. tuples
04. set

Set:    Set a items gular kono order thake na. So index number dile amra item khuje pabo na.
        Set a kono duplicate value rakha jabe na.
2 ways for makeing set: 01. Curley bracket.
                        02. set function.

Union       : |
Intersection: &
Difference  : -

'''

num1= {1,2,3,4,5}               #Use curley bracket for defining a set
num2= {1,2,3,4,5,5}             #If we creat with a duplicate value it shows only one
num3= set([4,5,6,7])            #First I creat a list then I convert that list into set.

num2.add(8)                     #We can add a value into the set
num2.remove(8)                  #Aso we can remove a value from the set

print(num1)
print(num2)
print(num3)

print(num1 | num3)              #Finding Union
print(num1 & num3)              #Finding Intersection
print(num1 - num3)              #Finding Difference

print(7 in num1)                #It shows true or false
print(5 in num3)                #It shows true or false
print(9 not in num2)            #It shows true or false
