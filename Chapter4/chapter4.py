
def computepay(h, r):
    if h > 40:
        overhrs = (h - 40)
        return overhrs * (r * 1.5) + (40 * rate)
    else:
        return h * r

hrs = input("Enter Hours: ")
hrs = float(hrs)
rate = input("Enter Rate: ")
rate = float(rate)
p = computepay(hrs, rate)
print(p)
