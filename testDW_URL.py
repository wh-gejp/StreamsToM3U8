#! /usr/bin/python3
import os
import sys

from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup

channels = []

def grab_youtube(user: str, secret: str, protected_url: str):
    """
Grabs the live-streaming M3U8 file from YouTube
    :param url: The YouTube URL of the livestream
    """
    url = 'https://accounts.google.com/login'
    if '&' in url:
        url = url.split('&')[0]

    requests.packages.urllib3.disable_warnings()
    session = requests.Session()
    session.post(url, data={'username': user, 'password': secret})
    response = session.get(protected_url)
    print(f"Status: {response.status_code}")
    print(response.text)
    
    """
    ua = UserAgent(os='Linux')
    ua.random    
    print(ua.random)
    header = {'User-Agent':str(ua.random)}
    #ua = UserAgent()
    #header = {'User-Agent':str(ua.chrome)}
    print(header)
    url = "https://www.youtube.com/watch?v=tZT2MCYu6Zw"
    stream_info = requests.get(url, headers=header)
    print(stream_info)
    """
    stream_info = response
    response = stream_info.text
    soup = BeautifulSoup(stream_info.text, features="html.parser")

    if '.m3u8' not in response or stream_info.status_code != 200:
        print("https://github.com/ExperiencersInternational/tvsetup/raw/main/staticch/no_stream_2.mp4")
        print(f'## Request    : {url}')
        print(f'## Status Code: {stream_info.status_code}')
        #print(f'## Response.Headers: {stream_info.headers}')
        #print(response)
        return
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end - tuner: end]:
            link = response[end - tuner: end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5

            stream_title = soup.find("meta", property="og:title")["content"]
            stream_desc = soup.find("meta", property="og:description")["content"]
            stream_image_url = soup.find("meta", property="og:image")["content"]
            channels.append((channel_name, channel_id, category, stream_title, stream_desc, stream_image_url))

            break
        else:
            tuner += 5
            print(f"{link[start: end]}")
            print (f'\n')

channel_name = 'DW News'
channel_id = 'DWNews.yt'
category = 'News'
logo = 'https://raw.github.com/wh-gejp/StreamsToM3U8/main/dw.png'
line = 'https://www.youtube.com/watch?v=tZT2MCYu6Zw'

if len(sys.argv) == 1:
    print(f'Len=1; Script: {sys.argv[0]}')
    print(f'User and Secure Token missing! Script will be terminated.')
    exit()
elif (len(sys.argv) == 2):
    print(f'Len=2; MUser: {sys.argv[0]}')
    print(f'Len=2; MUser: {sys.argv[1]}')
    print(f'Secure Token missing! Script will be terminated.')
    exit()
elif (len(sys.argv) == 3): 
    #print(f'Len=3; Script:  {sys.argv[0]}')
    #print(f'Len=3; MUser:   {sys.argv[1]}')
    #print(f'Len=3; MSecret: {sys.argv[2]}')
    mUser = {sys.argv[1]}
    mSecret = {sys.argv[2]}
    print (f'mUser: {mUser}, mSecret: {mSecret}')
    grab_youtube(mUser, mSecret, line)
else: 
    print(f'Len: {len(sys.argv)}')
    print(sys.argv[0])
    print(sys.argv[1])
    print(f'\nStartargument Länge: {len(sys.argv)}')
    print('Too many arguments! Script will be terminated.')
    exit()
            
# Remove temp files from project dir
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
