odd_list = [1,3,5,7]
even_list = [2,4,6,8]
#print(even_list)
dic = {
    "odd" : odd_list,
    "even" : even_list
}
for i in dic:
    temp = dic[i]
    for j in temp:
        print(j)