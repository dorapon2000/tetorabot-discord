import requests
from xml.etree import ElementTree

url = 'http://weather.livedoor.com/forecast/rss/primary_area.xml'
res = requests.get(url)
tree = ElementTree.fromstring(res.content)

with open('id_city_table', 'w', encoding='utf-8') as f:
    for pref in tree[0][12]:
        for city in pref[1:]:
            f.write('%s,%s\n' % (city.attrib['title'], city.attrib['id']))
