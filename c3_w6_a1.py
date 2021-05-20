import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
sum=0
while True:
    print('')
    url = input('Enter URL:')
    if (len(url) < 1): break
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    info = json.loads(data)
    info=info["comments"]
    for value in info:
        num1=value["count"]
        num=int(num1)
        sum=sum+num
    print(sum)
