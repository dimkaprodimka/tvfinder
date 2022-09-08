from bs4 import BeautifulSoup
import requests
from sys import argv

channel = argv[1]
user_ip = input('input ip acestream server for playlist 127.0.0.1 or remoteIP: ')
def get_tv_link(channel):
    url = f'https://acestreamsearch.net/?q={channel}'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    res = soup.find("ul", class_="list-group")
    a_tags = res.findAll('a')

    list_name = []
    list_href = []

    for a in a_tags:
        name = a.text
        href = a['href']
        print('{}\t{}'.format(name, href))
        list_name.append(name)
        list_href.append(href)
    return list_name, list_href

ln, lh = get_tv_link(channel)

#change http://38.242.159.189:6878 to you ip blaiseio/acelink server or docker

pl = '''#EXTINF:-1 group-title="TV",{}
http://{}:6878/ace/getstream?id={}
'''

with open(channel+'.m3u', 'w') as f:
    f.write('#EXTM3U\n')
    for a in range(len(ln)):
        f.write(pl.format(ln[a], user_ip, lh[a][12:]))

print(user_ip)
