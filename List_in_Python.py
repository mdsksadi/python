'''
In a variable we can assign only one value. But if we assing multiple values into the variable,
we need to use a list.
For diclaring a list, we need to use box bracket "[]"
We can assign both number and string type values.
List is mutable (We can chagne the values).
'''
nums= [2,4,20,54,120]       #We diclear a list and inside the lise we assign some values.
print(nums)

print(nums[0])              #It shows the 1st value. Position like [0 1 2 3 ..] 
print(nums[2])              #It shows the 3rd value.
#print(nums[10])             #IndexError: list index out of range.
print(nums[2:])             #Start at 3rd value and go till last.
print(nums[-1])             #Show the last value.

names = ["Shekh","Sadi","Tamim","Zahid","Anis","Rubel"] #We assing some string values.
print(names)

values = [20,25.5,"Rownak"] #We assing integer,float,string at a time.
print(values)               

mil= [nums,names]           #We can also assign nested list.
print(mil)

nums.append(45)             #We appned/add 45 at the last of the list.
print(nums)

#nums.clear                 #It will clear the eintier list

nums.insert(2,420)          #Add a value to a specific position. Here 2 is index number and 420 is the value
print(nums)

nums.remove(420)            #Remove a element by using "remove" 
print(nums)

nums.pop(2)                 #It pop up the 3rd value
print(nums)
nums.pop()                  #It maintains LIFO. So last value is removed
print(nums)

del nums[2:]                #Delete multiple values. Here we delete all starting 3rd value
print(nums)

nums.extend([5,3,1])        #We add some values into the list with "extend"
print(nums)

print(min(nums))            #We can see the munimum value by using inbuild function "min()"
print("The maximum value is: ",max(nums))  #We can see the maximum value by using inbuild function "max()"
print(sum(nums))            #The sum of all the values by using "sum()" function.

nums.sort()                 #Get all the values in sorted formet. Means ordering formet.
print(nums)

print("Physics" in names)   #Find the specefic result in the list
print("Tamim" in names)     #"Sensor" is not in the list
print("Sensor" not in names) #"not in" meant it's not in list. And it's true

print(names + ["Sensor", 25,30])     #Adding extra values in the list
print(nums * 3)                     #Shows the result 3 times
