fh = open("mbox-short.txt")
total = 0
n = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    n = n + 1
    pos = line.find(":")
    line = line[pos+1:].lstrip()
    total = total + float(line)
print("Average spam confidence:",total/n)