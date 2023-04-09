# Author: Norm McCord
# Date Created: 20230410
# Date Last Modified: 20230410
# Purpose: Ask user for input (nouns, verbs, adjectives).  Project focuses on creating and using variables and concatenation to manipulate strings.

# ask user for nouns, verbs, an adjective, and an adverb.  User input is string data type by default.
noun1 = input("Enter a noun: ")
verb1 = input("Enter a verb: ")
adjective1 = input("Enter an adjective: ")
noun2 = input("Enter another noun: ")
verb2 = input("Enter another verb: ")
adverb = input("Enter an adverb: ")

# print a sentence that concatenates the user input in a fun way
print("The", adjective1, noun1, "will", verb1, "over the", noun2, ", and", adverb, verb2)
# Python will put spaces in the output where the comma are by default.
