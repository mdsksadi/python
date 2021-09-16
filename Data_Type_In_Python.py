
'''
Data Type in Python:
--None
--Numeric
--List
--Tuple
--Set
--String
--Range
--Dictionray

'''
#None
'''
If I have a variable and on that variable if we do not asssign any value, is called "Nole".
In other langue we a keyword call "Null". But in Python we call it "None".
'''
#Numeric
'''
There are multiple types of Numeric datas.
Numeric:
--int
--float
--complex
--bool (True,False)

'''

num1=5
print("Type of num1 is: ",type(num1))           #It shows the type of "num1" is "<class 'int'>". 
                            #Because 5 is an integer number. So, "num1" is an integer type variable.

num2=2.5
print("Type of num2 is: ",type(num2))           #It shows the type of "num2" is "<class 'float'>"
                            #Because 2.5 is a float number. So, "num2" is a float type variable.

print(int(num2))                        #It's the conversion of float to int. And the resutl is 2
print(type(int(num2)))                  #It shows the type of the converted data "<class 'int'>"

print(float(num1))                      #It's the conversion of int to float. And the result is 5.0
print(type(float(num1)))                #It shows the type of the converted data "<class 'float'>"


num3=5+6j                               
print(num3)                             #Value of "num3" is "(5+6j)"
print(type(num3))                       #It shows the class of "num3" that is "<class 'complex'>"

num4=complex(num1,num2)
print(num4)                             #Value of "num4" is "(5+2.5j)""
print(type(num4))                       #It shows the class of "num4" that is "<class 'complex'>"

print(num1>num2)                        #Result of num1>num2 is "True"
print(type(num1>num2))                  #It shows the class of "True" and that is "<class 'bool'>"

print(num2>num1)                        #Result of num2>num1 is "False"
print(type(num2>num1))                  #It shows the class of "False" and that is "<class 'bool'>"

print(int(num1>num2))                   #We convert the value "True" into int and that is "1"
print(int(num2>num1))                   #We convert the value "False" into int and that is "0"
print(int(True))                        #We convert the value "True" into int and that is "1"
print(int(False))                       #We convert the value "False" into int and that is "0"

'''
Sequence:
There are various types of Sequences in Python:
--List
--Tuple
--Set
--String
--Range

'''
#List
L=[1,2,5,8,62,345]
print(L)                        #We can show the actual list: [1, 2, 5, 8, 62, 345]
print(type(L))                  #Here we can see the class of "list" and that is "<class 'list'>"

T=(2,6,5,7,9,5,20)
print(T)                        #We can see the actual tuple: (2, 6, 5, 7, 9, 5, 20)
print(type(T))                  #Here we can see the class of "Tuple" and that is "<class 'tuple'>"

S={1,5,6,8,6,20}
print(S)                        #We can see the actual set: {1, 20, 5, 6, 8}
print(type(S))                  #Here we can see the class of "set" and that is "<class 'set'>"

name="Shekh Sadi"
print(name)                     #Shekh Sadi
print(type(name))               #Here we can see the class of "String" is <class 'str'>

R1=range(10)
print(R1)                       #It auto set the initial value of the "range" and the value is: "range(0, 10)"
print(type(R1))                 #We can also see the class and that is <class 'range'>
print(list(R1))                 #For displaying all the value of range we make the list into set and the values are: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#print("\n")                    #We can diclare a new line by wirint "\n"

R2=range(0,10)
print(R2)                       #range(0, 10)
print(type(R2))                 #We can see the class of the "range" and that is: <class 'range'>
print(list(R2),"\n")            #For displaying all the value of range we make the list into set and the values are: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


R3=range(0,11,2)
print(R3)                       #We set a iteration of the range and now it is: range(0, 11, 2)
print(type(R3))                 #We can see the class of the "range" and that is: <class 'range'>
print(list(R3))                 #For displaying all the value of range we make the list into set and the values are: [0, 2, 4, 6, 8, 10]


#Maping or Dictionary

D={
    "Sadi":"POCO",
    "Zahid":"Xiaomi",
    "Anis":"Samsung",
    "Abbu":"Redmi"
}
print(D)                    #{'Sadi': 'POCO', 'Zahid': 'Xiaomi', 'Anis': 'Samsung', 'Abbu': 'Redmi'}
print(type(D))              #The class of D is: <class 'dict'>

print(D.keys())             #We can see the keys of the "Dictionary" by typing "D.key()" function and the result is: dict_keys(['Sadi', 'Zahid', 'Anis', 'Abbu'])
print(D.values())           #We can also see the values of the keys of the "Dictionary" by typing "D.values()" function and the result is: dict_values(['POCO', 'Xiaomi', 'Samsung', 'Redmi'])

print(D["Zahid"])           #We can also find the valu of every keys like "Zahid" and the output is "Xiaomi"
print(D.get("Sadi"))        #Similarly we can find the value of every keys by using get function and get the result like "POCO"

