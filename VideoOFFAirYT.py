#! /usr/bin/python3
import requests
import os

def grab(url):
    response = requests.get(url, timeout = 15).text
    if '.m3u8' not in response:
        print("https://bit.ly/3xRjEnQ")
        return
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end - tuner : end]:
            link = response[end - tuner : end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            break
        else:
            tuner += 5
    print(f"{link[start : end]}")

with open('./VideoOFFAirYT.txt', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('##'):
            continue
        if not line.startswith('https:'):
            line = line.split('-')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            print(f'\n#EXTM3U')
            print(f'\n#EXT-X-VERSION:3')
            print(f'\n#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=5400000')
        else:
            grab(line)
            
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
