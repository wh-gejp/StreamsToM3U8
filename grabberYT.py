#! /usr/bin/python3
import os
import sys

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
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
    #headers = {'Content-Type': 'text/html'}
    stream_info = requests.get(url, headers=headers, timeout=15)
    #stream_info = requests.get(url, timeout=15, allow_redirects = True)
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

channel_name = ''
channel_id = ''
category = ''
logo = ''
file_name = ''

# Open text file and parse stream information and URL
if len(sys.argv) == 1:
    file_name = './streams.txt'
else:
    if len(sys.argv) == 2:
        file_name = str(sys.argv[1])
        if not os.path.isfile(file_name):
            print(sys.argv[1])
            print('Argument must be an existing filename! Script will be terminated.')
            exit()
    else: 
        print(sys.argv[0])
        print(sys.argv[1])
        print(f'\nStartargument Länge: {len(sys.argv)}')
        print('Only one filename accepted! Script will be terminated.')
        exit()
#print(file_name)
with open(file_name, encoding='utf-8') as f:
    #if file_name == './streams.txt':
    print("#EXTM3U")
    for line in f:
        line = line.strip()
        if not line or line.startswith('##'):
            continue
        if not (line.startswith('https:') or line.startswith('http:')):
            line = line.split('||')
            channel_name = line[0].strip()
            channel_id = line[1].strip()
            category = line[2].strip().title()
            logo = line[3].strip()
            print(
                f'#EXTINF:-1 tvg-id="{channel_id}" tvg-name="{channel_name}" group-title="{category}" tvg-logo="{logo}", {channel_name}')
        else:
            grab_youtube(line)
            
# Remove temp files from project dir
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
