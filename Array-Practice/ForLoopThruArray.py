# array practice

arr = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in arr:
    print(i)


# range function stops at 1 less than the range; if no starting point range assumes "0"
for i in range(0, len(arr)):
    print(i)

# print index number with the contents of the array at each index
for i in range(0, len(arr)):
    print(i, arr[i])