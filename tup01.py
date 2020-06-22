hours = dict()
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
for line in handle:
    if line.startswith("From "):
        words = line.split()
        hour = words[5]
        hour = hour[:2]
        #print(hour)
        hours[hour] = hours.get(hour,0) + 1
#print(hours)
sorted_hours = sorted([(k,v) for k,v in hours.items()])
for k,v in sorted_hours:
    print(k,v)