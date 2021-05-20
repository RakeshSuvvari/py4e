name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_237680.txt"
handle = open(name)
count=0
import re
tfial=handle.read()
y=re.findall('[0-9]+',tfial)

for word in y:
    num=int(word)
    count=count+num
print(count)
#import re
#for line in handle:
#    y=re.findall('[0-9]+',line)
#    for word in y:
#        num=int(word)
#        count=count+num
#print(count)
