# Author: Norm McCord
# Date Created: 20230410
# Date Last Modified: 20230410
# Purpose: exercises in using files within a program

# opening a file
# mode: a string specifying how the file will be opened
    # Ex: reading only('r'), writing ('w'), appending ('a')
    # Reading: if the file exists, it opens and points to the beginning.  If it does NOT exist, you get an exception
    # Writing: if the file exists, DELETE IT AND CREATE AN EMPTY FILE OF THE SAME NAME, else create the file
        # Files should be closed using file object 'close' method to ensure the data was actually written to disk
            # - Format: file_variable.close() -
    # Appending: if the file exists, open it and point to the end for appending, else create it


# file_object = open(filename, mode)

f = open('demofile.txt', 'w') # everytime this block is run, the file is overwritten.  if the block is commented out, the next 2 block will append to, and read the file.
f.write("This is a demo text file.\nEnjoy.")
f.close()

f = open("demofile.txt", 'a')
f.write("\nThis is some more text appended to the file.")

f = open("demofile.txt", 'r')
print(f.read())

# e = open("demofile2.txt", "w")
# e.write("This is demo file #2.")
