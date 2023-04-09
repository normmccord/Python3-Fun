# A quick primer on strings in Python
# x and y are integers here
x = 2; y = 3
# print(x,y)
x += 1; y += x
# print(x,y)
# print(x+y)
# -----------------------------------------------------
# a and b are strings
a = "1"
b = "2"
print(a)
print(b)
a += b # this will 'append' b to the end of a and save it as a new value for a
# the new value for a is a string (12), not the number 12.  It's 1(&)2 next to each other.  the two characters are concatenated.
print(a)
print(a+b) # this will concatenate the 2 string variables next to each other.
print(a,b,x,y)
# c = a+x # this will throw an error since a is a string and x is an integer, and they can't be 'added' together
# print(c)

# a = "Hello"
# print(a[2]) # You can request the value at an index of the string just like an array
# for c in a: # you can iterate over a string just like an array
#     print(c)
# for i in range(0, len(a)):
#     print(a[i])

