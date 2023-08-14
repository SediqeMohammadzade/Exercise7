List_array = []
arr = int(input("Enter your array: "))
while arr != "end":
    List_array.append(arr)

print("List_arry:",List_array)

a = List_array
n = len(a)
for i in range(1,n):
    if a[i] < a[i-1]:
        print("It is sorted")
    else:
        print("it is not sorted")
List_array.sort()
print("True: ",List_array)

