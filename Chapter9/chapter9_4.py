name = input("Enter file:")
if len(name) < 1: name = "mbox.txt-short.txt"
handle = open(name)
counts = dict()

for line in handle:
    if 'From:' in line:
        continue
    if 'From' in line:
        words = line.split()
        # print(words)
        email = words[1]
        counts[email] = counts.get(email, 0) + 1

bigcount = None
bigword = None

for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)


