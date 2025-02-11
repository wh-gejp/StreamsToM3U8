#!/bin/bash
pwd
cat ./iptv1.m3u > ./iptv_liste.m3u
cat ./euronews.m3u >> ./iptv_liste.m3u
cat ./iptv2.m3u >> ./iptv_liste.m3u
cat ./dw.m3u >> ./iptv_liste.m3u
echo M3U files merge complete.
