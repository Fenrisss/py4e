# Use the file name mbox.txt-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
new_number = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    index = line.find(' ')
    a = line[index:]
    number = float(a.strip())
    # number = float(line[' '+3:])
    new_number = new_number + number
    count = count + 1
    average = new_number/count
print("Average spam confidence:", average)