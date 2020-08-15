
import json
import urllib.request
import urllib
url="http://py4e-data.dr-chuck.net/comments_837022.json"
u=urllib.request.urlopen(url)
data=u.read()
data=json.loads(data)



total=0
for tags in data['comments']:
      total+=tags["count"]
print(total)
