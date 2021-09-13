
'''
List: It's orderd. It's mantain the sequence.
Set: It does not maintain the sequence.

Dictionary: Differenty key for different element.
            Example: Phone book. If we search a name, we get a number against that name.
            Every value has a different key given by me.
            But in list, the key or index number is fixed and in set we can not define that.
key should be unike and immutable.

We use curly bracket "{}" for the dictrionary

'''
data = {1:"Shekh Sadi",2:"Zahid",4:"Anis"}  #We create a dictionary and set specific kes for every elements.
print(data)

print(data[1])          #We have to specifiy the key to fetch the value

#print(data[3])          #It shows error because we did not set any key called "3"
print(data.get(3))      #If we use "get" function, it does not show the error.
print(data.get(2,"Not found"))  ##We can also show a perticular message if the key is missing.
print(data.get(3,"Not found"))  #We can also show a perticular message if the key is missing.

mobile_number= {
    "Shekh Sadi":"+8801684443284",
    "Zahid":"+8801714498041",
    "Abbu":"+8801681303150",
    "Ammu":"+8801718529185"
}

print(mobile_number)

print(mobile_number["Abbu"])
print(mobile_number["Shekh Sadi"])
#print(mobile_number["Tamim])

print(mobile_number.get("Zahid","This number is not found"))
print(mobile_number.get("Tamim","This number is not found"))

#We can make it another way

who=["Sadi","Zahid","Anis","Rubel"]         #We declare a list
whom=["Rownak","Mim","Pinkey","vuila gesi"] #Declear another list
together=who+whom                           #Add to list into a single list
print(together)                             #Show the marged list
z=zip(whom,whom)                            #Zip the list
print(z)                #We can show the zipped code "<zip object at 0x0000028843247080>"
y=dict(z)
print(dict(y))          #Successfully we marged 2 list into a dictionary by "dict()" function

y["Roxy"]="Lichu"       #It added a key "Roxy" and element "Lichu"
print(dict(y))

del y["Roxy"]           #We deleted the key "Roxy" and it's value
print(y)

#Nested list and nested dictionary
prog={"Js":"Atom","CS":"VS","Python":["Pycharm","Sublime"],"Java":{"JSE":"Netbeams","JEE":"Eclipse"}}
print(prog)
print(prog["Js"])
print(prog["Python"])
print(prog["Python"][1])    #2nd set value of "Python"
print(prog["Java"])
print(prog["Java"]["JEE"])  #"JEE" value of key "Java"
