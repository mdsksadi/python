'''
Tuple is immutable. Because we can not change the value of tuple.
For defining a Tuple we need to use 1st bracket "()"

Tuples is like list. But the difference is, we can change the value of list.
But we can not change the vallue of Tuples.
Tuples is faster than list.

One more thing for memorising.
01. We use Squire Bracket"[]" for the list.
02. We use Curly Bracket "{}" for the set and dictionary.
03. We use First Bracket"()" for the Tuples.

'''

tup=(1,2,3,4,5)     #Define a tuple by using first bracket "()"
print(tup)

print(tup[1])       #Show the 2nd value

#tup[1]=10           #We can not chage the tuple. It shows "TypeError: 'tuple' object does not support item assignment"

print(tup.index(2))


students_name = (
    "Sheikh Sadi",
    ("Zahid Hossain", "Pada", 26, 1),   #It's called nested tuples.
    "Anis Sarker",
    "Abdur Rahman"

)

#students_name[0]= "Adis"            #It will not work. Because we can not change the value of tuples.

print(students_name[1])

