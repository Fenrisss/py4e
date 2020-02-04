import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# url = input('Enter location: ')
url = 'http://py4e-data.dr-chuck.net/comments_337460.xml'

count = 0
sum = 0

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
# print(data.decode)
tree = ET.fromstring(data)
numbers = tree.findall('.//count')

for i in numbers:
    sum = sum + int(i.text)
    count = count + 1

print("Count: ", count)
print("Sum: ", sum)

