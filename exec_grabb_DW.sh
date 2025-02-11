#!/bin/bash
python3 -m pip install requests
python3 -m pip install beautifulsoup4

python3 grabberOD.py dw.txt > ./dw.m3u

echo dw.m3u update complete.
