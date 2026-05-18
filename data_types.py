import math
# String data type

# Literal assignment
first = "Dave"
last = "Gray"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# Constructor function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(first, str))

# Concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I love rock music from the " + decade + "s."
print(statement)

# Multiple lines
multiline = """
Hey!, How are you?

I was just checking in.

All good?

"""

print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# String Methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                                    "
multiline = "                                     " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")
# Build a menu 
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(0))
print("Muffin".ljust(16, ".") + "$2".rjust(0))
print("Cheesecake".ljust(16, ".") + "$4".rjust(0))

print("")

# String index value
print(first[0])
print(first[-1])
print(first[1: -1])
print(first[1:])

# Some methods that return boolean data
print(first.startswith("D"))
print(first.endswith("Z"))

# Boolean data type
my_value = True
x = bool(False)
print(type(x))
print(isinstance(my_value, bool))

# Numeric data types

# Integer
price = 100
best_price = int(80)

print(type(price))
print(isinstance(best_price, int))

# float data type
GPA = 3.56
Y = float(1.14)

print(type(GPA))

# Complex type
comp_value = 5 + 3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in functions for numbers
print(abs(GPA))
print(abs(GPA * -1))

print(round(GPA))

print(round(GPA, 1))


print(math.pi)
print(math.sqrt(64))
print(math.ceil(GPA))
print(math.floor(GPA))

# Casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))
