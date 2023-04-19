# Author: Norm McCord
# Date Created: 20230412
# Date Last Modified: 20230412
# Purpose: exercises in using files within a program

# write 2 programs to operate on variables a, b, and c.  The 1st program will write all 3 variables to a file, the 2nd (see FileIOp2) will read the file and place the data back into the three respective variables

a = 1234.2345
b = "Hello there."
c = True

# program 1
# use something to separate the data for readability (like a tab character)
f = open('demofile3.txt', 'w')
f.write(str(a) + "\t")
f.write(b + "\t")
f.write(str(c) + "\t")

# remember to close the file
f.close()