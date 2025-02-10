#!/bin/bash
python3 -m pip install requests
python3 -m pip install html5lib
python3 -m pip install beautifulsoup4

python3 grabberOD.py euronews.txt > ./euronews.m3u

echo euronews.m3u update complete.
