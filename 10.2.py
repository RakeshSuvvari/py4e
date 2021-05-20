name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts=dict()
for line in handle:
    if line.startswith('From '):
        spl=line.split()
        time=spl[5]
        timesp=time.split(':')
        hour=timesp[0]
        counts[hour]=counts.get(hour,0)+1
for k,v in sorted(counts.items()):
    print(k,v)
