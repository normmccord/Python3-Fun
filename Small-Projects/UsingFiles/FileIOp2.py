# Author: Norm McCord
# Date Created: 20230412
# Date Last Modified: 20230412
# Purpose: exercises in using files within a program

# write 2 programs to operate on variables a, b, and c.  The 1st program (see FileIOp1) will write all 3 variables to a file, the 2nd will read the file and place the data back into the three respective variables

x = None
y = None
z = None

# program 2
# use something to separate the data for readability (like a tab character)
f = open('demofile3.txt', 'r')

line = f.readline()
fields = line.split("\t") # like using string.split at 'tab' character
# print(fields) # uncomment to print the array

# after reading the file, we've written the program to assign file contents into the following variables
x = float(fields[0])
y = fields[1]
z = bool(fields[2])

print(x, y, z)
# print(type(x), type(y), type(z)) # uncomment to print the variable types

# remember to close the file
f.close()
