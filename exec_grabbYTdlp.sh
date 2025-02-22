#!/bin/bash
User=$1
Secret=$2
echo "User: ${User} :"
# echo "Secret User: ${{ secrets.MAIL_USER}} :" # git hub Variable will not be substituted
./yt-dlp_2025.02.19 -u ${User} -p ${Secret} -f 95 -g http://www.youtube.com/watch?v=CQ3KsEbsYHs > testYTdlp.txt
echo testYTdlp.txt complete.
