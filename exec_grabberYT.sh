#!/bin/bash
echo $1
python3 -m pip install requests
python3 -m pip install beautifulsoup4

python3 grabberYT.py $1.txt > $1.m3u

echo $1.m3u update complete.
