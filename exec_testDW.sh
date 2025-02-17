#!/bin/bash
$User = $1
echo "User: ${User} :"
python3 -m pip install requests
python3 -m pip install fake-useragent
python3 -m pip install beautifulsoup4
python3 testDW_URL.py  ${User} > testDW.txt
echo testDW.txt complete.
