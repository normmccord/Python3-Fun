# array practice

arr = ["red", "orange", "yellow", "green", "blue", "purple"]
i = int(input("enter an index number: "))
# i = int(input("enter an index number: "))
# while i >= 0 and i <= len(arr)-1:
#     print(arr[i])
#     i = int(input("enter an index number: "))

if i >= 0 and i <= len(arr)-1:
    print(arr[i])
else:
    print("Your index is invalid")