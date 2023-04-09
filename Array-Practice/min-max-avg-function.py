# there's a function for that
import random

x = 0
y = 25
n = 25

arr = [0] * n # gives a N-element array with each element being 0

for i in range(0, len(arr)):
    arr[i] = (random.randint(x, y))
print(arr)

print("Max = ", max(arr))
print("Min = ", min(arr))
print("Avg = ", sum(arr)/len(arr))