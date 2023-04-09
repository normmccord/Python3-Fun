# Stringing Strings together
# Write a program that prompts the user for 3 strings
# Concatenate the strings together and count the number of occurences of the letter 'e'

# Remember: a string is just an array

# prompt for 3 strings
a = input("String 1: ")
b = input("String 2: ")
c = input("String 3: ")
print("When using 'print' command with commas separating the variables you get: '"+a,b,c+"'")

# Concatenate them together
d = a + b + c
print("When concatenating the variables into one new variable using a '+' and printing that new variable, you get: '"+d+"'")

# Count the 'e's
e_count = 0
for c in d: # you can iterate over a string just like an array
    if c == "e":
        e_count += 1

print("Number of E's: "+str(e_count))
