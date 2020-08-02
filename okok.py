
import json
import urllib.request
import urllib
import xml.etree.ElementTree as ET
url=" http://py4e-data.dr-chuck.net/comments_837021.xml"
u=urllib.request.urlopen(url)
data=u.read()
xml_data=ET.fromstring(data)
search_str="comments/comment"
count_tags=xml_data.findall(search_str)

total=0
for tags in count_tags:
      c=tags.find('count')
      total+=int(c.text)
print(total)
