from bs4 import BeautifulSoup
import requests
from sys import argv

channel = argv[1]



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


tpl = input('Select type Playlist: 1-Acestream 2-VLC: ')

if tpl == '1':
    pl = '''
#EXTINF:-1 group-title="{}",{}
{}
    '''
    with open(channel+'.m3u', 'w') as f:
        f.write('#EXTM3U\n')
        for a in range(len(ln)):
            f.write(pl.format(channel, ln[a],  lh[a]))
            
elif tpl == '2':
    user_ip = input('input ip acestream server for playlist 127.0.0.1 or remoteIP: ')

    pl = '''
#EXTINF:-1 group-title="{}",{}
http://{}:6878/ace/getstream?id={}
    '''

    with open(channel+'.m3u', 'w') as f:
        f.write('#EXTM3U\n')
        for a in range(len(ln)):
            f.write(pl.format(channel, ln[a], user_ip, lh[a][12:]))

    print('playlist for ' + user_ip + ' created')
else:
    print('bad choys bye bye')


