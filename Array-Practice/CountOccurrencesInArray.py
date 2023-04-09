# Count occurrences of a given number in an array

arr1 =[1, 6, 8, 2, 4, 7, 9, 3, 5, 4, 1, 7, 8, 3, 5, 6, 7, 1]
x = int(1)
y = int(10)

# iterate over the range and do a sequential search to find instances of each number
for i in range(x, y+1):
    # count occurrences
    found_count = 0
    for j in arr1:
        if i == j:
            found_count += 1
    print(i, ":", found_count)

# Alternate method using iteration over the range
for i in range(x, y+1):
    # count occurrences
    found_count = 0
    for j in range(0, len(arr1)):
        if i == arr1[j]:
            found_count += 1
    print(i, ":", found_count)