import urllib.request, urllib.parse ,urllib.error
from bs4 import BeautifulSoup
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

link = "http://py4e-data.dr-chuck.net/comments_42.xml"
html=urllib.request.urlopen(link, context=ctx).read()
soup=BeautifulSoup(html,'html.parser')


xml_data=ET.fromstring(data)
search_str="comments/comment"
count_tags=xml_data.findall(search_str)

total=0
for tags in count_tags:
      c=tags.find('count')
      total+=int(c.text)
print(total)