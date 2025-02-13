#!/bin/bash
mergeFile='iptv_liste'
cat ./iptv1.m3u > ./$mergeFile.m3u
cat ./euronews.m3u >> ./$mergeFile.m3u
cat ./iptv2.m3u >> ./$mergeFile.m3u
cat ./dw.m3u >> ./$mergeFile.m3u
echo M3U files merge to $mergeFile complete.
