import re
num = list()
handle = open("regex_sum_692721.txt")
for line in handle:
    if re.search('[0-9]+',line):
        tmp = re.findall('[0-9]+',line)
        for number in tmp:
            num.append(int(number))
print(sum(num))
    