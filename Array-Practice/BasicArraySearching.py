# array practice

arr = ["red", "orange", "yellow", "green", "blue", "purple"]


c = input("Enter a color: ")

# declare a flag to help stop the loop
found = False

for i in range(0, len(arr)):
    if arr[i] == c:
        print(c + " is in index " + str(i))
        found = True
        break

if not found:
    print(-1)

print("Done")