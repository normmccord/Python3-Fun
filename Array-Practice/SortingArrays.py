# array practice

arr = ["red", "orange", "yellow", "green", "blue", "purple"]

# bubble sort
def bubble_sort(arr):
    l = len(arr)
    for i in range(l-1):
        flag = 0
        for j in range(0, l-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                flag = 1
                if flag == 0:
                    break
    return arr

# prints sorted array using the new method
print(bubble_sort(arr))



# Python has a sorting function built-in
# arr.sort()
# print(arr)