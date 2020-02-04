fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    list = line.split()
    for i in list:
        if lst is None:
            lst.append(i)
        if i not in lst:
            lst.append(i)
lst.sort()
print(lst)



