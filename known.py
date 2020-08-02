import urllib.request, urllib.parse ,urllib.error
from bs4 import BeautifulSoup
import ssl
import urllib

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

link = input("Enter URL:")
count=int(input("Enter count:"))
pos=int(input("Enter line:"))

print("Retrieving",link)
for i in range(0,count):
    html=urllib.request.urlopen(link).read()
    soup=BeautifulSoup(html)
    tags=soup('a')

    link=tags[pos-1].get('href')

result=tags[pos-1].contents[0]
print(result)