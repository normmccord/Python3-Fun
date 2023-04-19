# Author: Norm McCord
# Date Created: 20230412
# Date Last Modified: 20230419
# Purpose: A program that reads a file containing average daily rainfalls for each month and prints the average rainfall for each month
# Reference:
    # Lecture at Kennesaw State University, IT 1114 Programming Principles Spring '23, Module 10

f = open('rainfall.txt', 'r') # 'f' is the name we will give to the FILE OBJECT

for line in f:
    total = 0
    fields = line.strip().split(" ") # much shorter way of writing the loop
    for i in range(1, len(fields)):
        total += float(fields[i])
    print(fields[0], (total/(len(fields)-1)))



