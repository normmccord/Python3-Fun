# Author: Norm McCord
# Date Created: 20230419
# Date Last Modified: 20230419
# Purpose: Given a network log (txt file), count the number of packets that were sent from each independent source address
# Reference:
    # Lecture at Kennesaw State University, IT 1114 Programming Principles Spring '23, Module 10

    # the associated "network-log.txt file is removed from the folder before updating to GitHub

addr = {} # this is a hash table, or dictionary
file_in = open('network-log.txt', 'r') # open the file 'network-log.txt' (use your own text file that is hopefully delineated in some way) and assign it to the file object that we've named 'file_in'
net_log = file_in.readline() # Read a line (these are headers we want to ignore)
net_log = file_in.readline() # Read the first line of actual data

# get source addresses
while net_log != "":
    data = net_log.split("\t") # the file I used was delineated by tabs. Yours may be commas or something else...
    # if we've not seen the address yet, add address to list of addresses we've seen, set its counter to 1, else, add 1 to that address's counter
    if data[2] not in addr:
        addr[data[2]] = 1
    else:
        addr[data[2]] += 1
    net_log = file_in.readline()  # Read the next line of actual data


for k in addr.keys():
    print(k, "-", addr[k]) # this will show the IP addresses and their counts from the network-log.txt file
