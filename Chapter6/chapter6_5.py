text = "X-DSPAM-Confidence:    0.8475";

# find = text.find("0.8475")
# number = text[find:]
# fnumber = float(number)
# print(fnumber)

find = text[23:]
fnumber = float(find)
print(fnumber)