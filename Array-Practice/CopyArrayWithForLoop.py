# array practice

arr = ["red", "orange", "yellow", "green", "blue", "purple"]
arr.append("cyan")

# use a for loop to copy the contents of one array into another
arr2 = [None] * len(arr)

for i in range(len(arr)):
    arr2[i] = arr[i]

print(arr2)

arr2.sort()
print(arr2)