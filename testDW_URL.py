#! /usr/bin/python3
import os
import sys

from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup

channels = []

def grab_youtube(url: str):
    """
Grabs the live-streaming M3U8 file from YouTube
    :param url: The YouTube URL of the livestream
    """
    if '&' in url:
        url = url.split('&')[0]

    requests.packages.urllib3.disable_warnings()
   
    ua = UserAgent()
    print(ua.chrome)
    header = {'User-Agent':str(ua.chrome)}
    print(header)
    url = "https://www.youtube.com/watch?v=tZT2MCYu6Zw"
    stream_info = requests.get(url, headers=header)
    print(stream_info)
   
    response = stream_info.text
    soup = BeautifulSoup(stream_info.text, features="html.parser")

    if '.m3u8' not in response or stream_info.status_code != 200:
        print("https://github.com/ExperiencersInternational/tvsetup/raw/main/staticch/no_stream_2.mp4")
        print(f'## Request    : {url}')
        print(f'## Status Code: {stream_info.status_code}')
        print(f'## Response.Headers: {stream_info.headers}')
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
logo = 'https://raw.github.com/wh-ge/StreamsToM3U8/main/dw.png'
line = 'https://www.youtube.com/watch?v=tZT2MCYu6Zw'

grab_youtube(line)
            
# Remove temp files from project dir
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
