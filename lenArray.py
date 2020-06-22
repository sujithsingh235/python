a = []
onerow = []
row = int(input("Enter the number of rows:"))
col = int(input("Enter the number of cols:"))
for i in range(row):
    for j in range(col):
        onerow.append(int(input()))
    a.append(onerow.copy())
    onerow.clear()
print(a)
print(a[1][1])
