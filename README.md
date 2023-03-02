# acestream playlist creator
Use:
tvfinder-docker.py <channel or preffix like [pl]> <format playlist: ace,vlc> <ip acestream-server, or none>
example:
python3 tvfinder-docker.py hbo ace n
python3 tvfinder-docker.py hbo vlc 127.0.0.1

Docker:
docker build -t tvfinder . 
docker run --rm -a stdout --name tv tvfinder:latest hbo vlc 127.0.0.1    "or add"  > channel.m3u


python3 tvfinder.py <channel or prefix>
example: 
python3 tvfinder.py sport

select format playlist acestream 
or m3u for vlc and iptv, next write ip addr acestream server (default localhost: 127.0.0.1)

example python3 tvfinder.py pl]
