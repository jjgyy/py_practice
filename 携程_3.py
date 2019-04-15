# -*- coding: utf-8 -*-
import sys
type = sys.getfilesystemencoding()
line = sys.stdin.readline().strip()

print line.decode('UTF-8').encode(type)

cities = line.split('|')

info = {}
for index in range(26):
    info[index] = []



for city in cities:
    city_infos = city.split(',')
    city_short = city_infos[1]
    info[ord(city_short[0]) - ord('a')].append(city_infos)

result = ''

for key in info:
    if info[key] == []:
        continue
    else:
        info[key].sort(key=lambda e: e[2])
        result += chr(ord('a') + int(key))
        result += ':'
        city_list = info[key]
        for city_object in info[key]:
            city_str = city_object[0] + ',' + city_object[1] + ',' + city_object[2] + '|'
            result += city_str
        result = result[:-1]
        result += '#'

if result[-1] == '#':
    result = result[:-1]

print result.decode('UTF-8').encode(type)