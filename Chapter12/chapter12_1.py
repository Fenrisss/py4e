from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
total = 0
# Retrieve all of the anchor tags
tags = soup('span')

for tag in tags:
    x = re.findall("[0-9]+", str(tag))
    for i in x:
        i = int(i)
        total = total + i
print(total)

