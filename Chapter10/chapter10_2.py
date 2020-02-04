name = input("Enter file:")
if len(name) < 1 : name = "mbox.txt-short.txt"
handle = open(name)

counts = dict()

for line in handle:

    if 'From:' in line:
        continue
    if 'From' in line:
        print(line)
        words = line.rstrip().split(':')
        first_index = words[0]
        hour = first_index[-2:]
        counts[hour] = counts.get(hour, 0) + 1

print(type(counts))
tmp = list()
for k, v in counts.items():
    tmp.append((k, v))
    tmp.sort(reverse=False)
for p in tmp:
    print(p[0], p[1])

# bigcount = None
# bighour = None
#
# for h, count in counts.items():
#     if bigcount is None or count > bigcount:
#         bighour = h
#         bigcount = count
# print(bighour, bigcount)


#Submitted code:
# name = input("Enter file:")
# if len(name) < 1 : name = "mbox.txt-short.txt"
# handle = open(name)
# counts = dict()
#
# for line in handle:
#     if 'From:' in line:
#         continue
#     if 'From' in line:
#         words = line.rstrip().split(':')
#         first_index = words[0]
#         hour = first_index[-2:]
#         counts[hour] = counts.get(hour, 0) + 1
#
# tmp = list()
# for k, v in counts.items():
#     tmp.append((k, v))
#     tmp.sort(reverse=False)
# for p in tmp:
#     print(p[0], p[1])