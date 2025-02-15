#!/bin/bash
python3 -m pip install requests
python3 -m pip install fake-useragent
python3 -m pip install beautifulsoup4
python3 testDW_URL.py > testDW.txt
echo testDW.txt complete.
