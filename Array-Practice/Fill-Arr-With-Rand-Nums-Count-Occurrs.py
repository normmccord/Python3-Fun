import random

x = 1
y = 10
n = 10
# declare an array of N elements
# populate array with a range of random numbers

# two ways

# option 1
# arr1 =[0] * 10# populates a 10-element array with each element being a 0
# for i in range(0, len(arr1)):
#     arr1 = random.randint(1, 10)

# option 2
arr1 = [] # Declare an empty array and append the desired number of elements to it
for i in range(n):
    arr1.append(random.randint(x, y))

# populate with random numbers between x and y

# iterate over the range and do a sequential search to find instances of each number
for i in range(x, y+1):
    found_count = 0
    if i in arr1: # only if 'i' exists in the array, then count, otherwise skip
        # count occurrences
        for j in arr1:
            if i == j:
                found_count += 1
        print(i, ":", found_count)