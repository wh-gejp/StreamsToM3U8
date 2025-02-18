#!/bin/bash
User=$1
Secret=$2
echo "User: ${User} :"
# echo "Secret User: ${{ secrets.MAIL_USER}} :"
python3 -m pip install requests
python3 -m pip install fake-useragent
python3 -m pip install beautifulsoup4
python3 testDW_URL.py  ${User} ${Secret}> testDW.txt
echo testDW.txt complete.
