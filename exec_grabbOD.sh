#!/bin/bash
python3 -m pip install requests
python3 -m pip install bs4
python3 -m pip install beautifulsoup4

python3 grabberOD.py euronews.txt > ./euronews.m3u

echo euronews.m3u update complete.
