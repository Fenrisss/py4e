import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
count = 0
sum = 0
x = []

address = input('Enter location: ')
print('Retrieving', address)
connection = urllib.request.urlopen(address, context=ctx)
data = connection.read()
# print(data)
print('Retrieved', len(data), 'characters')
data = json.loads(data)
# print(data['comments'][3]['count'])
for i in range(0, 50):
    x = i
    number = data['comments'][x]['count']
    sum = sum + number
    count = count + 1
print('Count:', count)
print('Sum:', sum)
# for key, value in data.items():
#     print(type(value))
# print('+++\n', data, type(data))


# ____________________________________________________
# import json
#
# data = '''
# [
#   { "id" : "001",
#     "x" : "2",
#     "name" : "Chuck"
#   } ,
#   { "id" : "009",
#     "x" : "7",
#     "name" : "Brent"
#   }
# ]'''
#
# info = json.loads(data)
# print('User count:', len(info))
#
# for item in info:
#     print('Name', item['name'])
#     print('Id', item['id'])
#     print('Attribute', item['x'])