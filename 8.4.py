fname =input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    #ls= line.rstrip()
    lsp=line.split()
    for element in lsp:
        if element in lst:
            continue
        else :
            lst.append(element)
lst.sort()
print(lst)
