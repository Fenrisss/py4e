import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
# count = input('Enter count: )
# position = input('Enter position: )
# url = 'http://py4e-data.dr-chuck.net/known_by_Aleksandra.html'
count = input('Enter count: ')
count = int(count)
position = input('Enter position: ')
position = int(position)
print("Processing...")
for loop in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    number = 0
    for tag in tags:
        number = number + 1
        if number == position:
            url = tag.get('href', None)
            if loop == count - 1:
                print(tag.contents[0])
