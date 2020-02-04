# Use words.txt as the file name
fname = input("Enter file name: ")
# fh = open(fname, 'r').read().upper().strip()
file = open(fname)

for line in file:
    print(line.upper().strip())


