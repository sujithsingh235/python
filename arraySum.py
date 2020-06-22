a = []
b = []
c = []
print("Enter first array:")
for i in range(4):
    a.append(int(input()))
print("Enter second array:")
for i in range(4):
    b.append(int(input()))
print("The sum array is....")
for i in range(4):
    c.append(a[i] + b[i])
for i in range(2):
    for j in range(2):
        print(c[j+i],end=" ")
    print()