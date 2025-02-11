#!/bin/bash
python3 -m pip install requests
python3 -m pip install lxml
python3 -m pip install pytz
python3 -m pip install beautifulsoup4
python3 grabber.py euronews.txt > ./euronews.m3u
echo M3U update complete.
