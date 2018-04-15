# -*- coding: utf-8 -*-
import requests
from random import choice

def geo_search(lan1,lan2,lon1,lon2):
    try:
        api_url_base = 'https://api.wigle.net/api/v2/network/search?onlymine=false&latrange1=' + str(lan1) + '&latrange2=' + str(lan2) + '&longrange1=' + str(lon1) + '&longrange2=' + str(lon2) + '&freenet=false&paynet=false'
        
        proxy_list = ['87.98.174.157:3128','91.240.87.109:3130']
        proxy = {'https':'https://' + str(choice(proxy_list))}
        
            
        headers_list = ['QUlEMzgwZDY3ZjQ1YWRkMTdlYTQxYzJjZjdjOWZkYWQ0Zjc6ZTdiZjQ3ZWMzOWI2YmI0MDJhN2U1MjgxNjM5MzBiOTc=','QUlENjAyZWM3M2I3Y2E1MzUyZThmZTYzNGVkOGNkNzcxODg6YmY4Y2M4NGQ0NWIxOGJhYTZlNGI0ODljNjBmZTgzOWM=']
            
        headers = {'Content-Type': 'application/json',
           'Authorization': 'Basic ' + str(choice(headers_list))}
        
        
            
        r = requests.get(api_url_base, headers=headers, proxies=proxy)
            
        data = r.json()['results']
            
        bssid = []
        for n in range(len(data)):
            bssid.append(data[n].get('netid'))
            
        
        
        wifi_url = 'https://3wifi.stascorp.com/api/apiquery?key=MHgONUzVP0KK3FGfV0HVEREHLsS6odc3&bssid='
        
        mesg = 'Я нашел пароли от этих wifi ситей:' + '\n' + '\n'
        for b in bssid:
            find = requests.get(wifi_url + b)
            if find.json()['data'] != []:
                for lis in ('bssid','essid','key','wps'):
                    mesg += str(lis)
                    mesg += ': '
                    mesg += str(find.json()['data'][b][0][lis])
                    mesg += '\n'
                mesg += '\n'
        
        if mesg == 'Я нашел пароли от этих wifi ситей:' + '\n' + '\n':
            return 'Я не знаю паролей от сетей wifi каторые рядом с вами'
        else:
            return mesg
        
    except Exception as e:
        return 'Что-то пошло не так,попробуйте еще раз'
    