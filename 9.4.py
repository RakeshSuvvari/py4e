name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts=dict()
for line in handle:
    line=line.rstrip()
    if line.startswith('From '):
        words=line.split()
        word=words[1]
        #for word in words:
        #    if word==words[1]:
        counts[word]=counts.get(word,0)+1

largest=-1
max_word=None
for k,v in counts.items():
    if v>largest:
        largest=v
        max_word=k
print(max_word,largest)
