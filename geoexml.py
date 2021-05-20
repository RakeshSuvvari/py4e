from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url =input('Enter location: ')
print('Retrieving', url)
uh =urlopen(url, context=ctx).read()

print('Retrieved',len(uh),'characters')
tree = ET.fromstring(uh)
counts= tree.findall('.//count')
tot=0
for i in range(0,len(counts)):
    tot += int(counts[i].text)
print(tot)
