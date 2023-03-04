from bs4 import BeautifulSoup
import requests
from sys import argv


channel = argv[1]
choys = argv[2]
ip = argv[3]


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
#        print('{}\t{}'.format(name, href))
        list_name.append(name)
        list_href.append(href)
    return list_name, list_href

ln, lh = get_tv_link(channel)

if choys == 'ace':
    pl = '''
#EXTINF:-1 group-title="{}",{}
{}
    '''
    print('#EXTM3U\n')
    for a in range(len(ln)):
        print(pl.format(channel, ln[a],  lh[a]))
            
elif choys == 'vlc':
    user_ip = ip

    pl = '''
#EXTINF:-1 group-title="{}",{}
http://{}:6878/ace/getstream?id={}
    '''

    print('#EXTM3U\n')
    for a in range(len(ln)):
        print(pl.format(channel, ln[a], user_ip, lh[a][12:]))

else:
    print('bad choys bye bye')


