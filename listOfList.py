list1 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
for i in list1:
    for j in i:
        print(type(i))
        print(j,end=" ")
    print()