name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
mail = {}
for line in handle:
    if line.startswith("From "):
        words = line.split()
        sender = words[1]
        mail[sender] = mail.get(sender,0)+1
Bigsender = None
Bigtimes = None
for sender in mail:
    times = mail[sender]
    if Bigsender is None or Bigtimes<times:
        Bigsender = sender
        Bigtimes = times
print(Bigsender,Bigtimes)