'''def Hello():
    print("Thank you!")
n = int(input("Enter the number of elements:"))
arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j]>arr[j+1] :
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
    print("step ",i,":",arr,end="<==\n")
    Hello()
print(arr)'''
lst = [5,3,6,4,6,1]
lst.sort(reverse = True)
print(lst)