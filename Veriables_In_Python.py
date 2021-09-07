"""
Variable means the result could be varied. We can change the value of the variable anytime.
We can modefy the variable and set a new value.

"""


x=2             #we just diclare a variable "x" and put a value 2 inside of the variable "x"
print(x+3)      #Inside the print function we add a number with the variable and it shows the actual result

y=3             #We diclear another variable "y" and put a value 3 inside the variable "y"
print(x+y)      #Now we are adding two variables and get the actual result

x=9             #We just set a new value to the variable x
print(x+y)      #Here we get that the result is 12 instead of 5. Because the value of the variable "x" is changed.

print(x)        #It shows the result 9. It's the new value. Because the value is modefied.

#abc             #It shows error and give a message that "name 'abc' is not defined"

print(x+y)
#print(_+10)     #"_" means the result of previous operation. Although it's not working here. Maybe this IDE does not support it.

name = "Shekh Sadi"     #Also we can use variable fot the string type value
print(name)             #It shows "Shekh Sadi" which is the actual value
print(name + " is living in Coburg")    #We can add a string type variable with a string
print (name + " is",25,"years old")     #Also we can add variable, string, number at the same time

print(name[0])          #It shows the 1at charector of the variable "name"
print(name[2])          #It shows the 3rd charector of the variable "name"
print(name[-1])         #It shows the last charector of the variable "name"
#print(name[12])         #It shows "IndexError: string index out of range" because we don't have so many charector in the variable "name"
print(name[0:2])        #It shows 1st 2 charectors. Because 0 menas start with 1st charector and 2 means it will show total 2 charectors.
print(name[2:])         #It stats from 3rd Charector and go till end
print(name[:4])         #It start from 1st Charector and show intoal 4 words
print(name[3:20])       #It start from 4th charector and go till possible
print(name[0:8:2])      #It start on 1st charector. Goes till 8th charector and charector interval is 2. So it skips every 1 charector after

#print(name[0:3]=my)     #It shows error. Because string value can not be changed in python
print("My nick name is only "+name[6:]) #But we can change the string like this

print(len(name))        #We can also find the length of the variable just using len() function

