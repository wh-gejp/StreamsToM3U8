#!/bin/bash
python3 -m pip install beautifulsoup4 requests

python3 grabberOD.py euronews.txt > ./euronews.m3u

echo euronews.m3u update complete.
