import re
file = input('File name: ')
handle = open(file)

# handle = open('text')
sum = 0

for line in handle:
    line = line.strip()
    y = re.findall("([0-9.]*[0-9]+)", line)
    if len(y) == 0:
        continue
    for i in y:
        i = float(i)
        if sum is None:
            sum = sum + i
        else:
            sum = sum + i
sum = int(sum)
print(sum)