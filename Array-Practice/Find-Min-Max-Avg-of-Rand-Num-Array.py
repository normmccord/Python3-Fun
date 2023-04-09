# generate an array of N random numbers
# find the index of the minimum value
# find the index of the maximum value
# find average of all values in the list
import random

def max(arr):
    if len(arr) < 1:
        return -1
    else:
        i_max = 0
        for i in range(len(arr)):
            if arr[i] > i_max:
                i_max = i
        return i_max

def min(arr):
    if len(arr) < 1:
        return -1
    else:
        i_min = 0
        for i in range(len(arr)):
            if arr[i] < arr[i_min]:
                i_min = i
        return i_min

def avg(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum/len(arr)



x = 0
y = 25
n = 25

arr = [0] * n # gives a N-element array with each element being 0

for i in range(0, len(arr)):
    arr[i] = (random.randint(x, y))
print(arr)

print("Max = ", arr[max(arr)])
print("Min = ", arr[min(arr)])
print("Avg = ", avg(arr))