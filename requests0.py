# -*- coding: utf-8 -*-

import requests

#r = requsts.get('https://xkcd.com/353/')
#print(r.text) # html --> then html parser

r = requests.get('https://imgs.xkcd.com/comics/python.png')
print(r.content)

with open('comic2.png', 'wb') as f:
    f.write(r.content)

ok = r.ok # !!! https://www.youtube.com/watch?v=yqm6MBt-yfY

#rBin = requests.get()
rBin = requests.get('https://httpbin.org/get?page=2&count=25')
print('-----')
print(rBin.url)
print(rBin.text)

payload = {'page': 2, 'count':25}
rBin2 = requests.get('https://httpbin.org/get', params=payload)

payloadPost = {'username': 'corey', 'password': 'testing'}
rBinPost1 = requests.post('https://httpbin.org/get', data=payloadPost)

# !!!
# print(r.json()) # JSONDecodeError: Expecting value
# r_dict = r.json()
#     rdict['form'] # password, testing
#### equivalent to:
# import json
# json.loadS()

######################------------COOKIES--------------




################-------------  AUTHORIZATION ##################
rBinAuth0 = requests.get('https://httpbin.org/basic-auth/corey/testing', auth = ('corey', 'testing2'))
# <Response [401]>

rBinAuth1 = requests.get('https://httpbin.org/basic-auth/corey/testing', auth = ('corey', 'testing'))
# rBinAuth1 # <Response [200]>
print(rBinAuth1.text)
# '{\n  "authenticated": true, \n  "user": "corey"\n}\n'


rDelay1 = requests.get('https://httpbin.org/delay/1', timeout=3)
# 200
rDelay3_2 = requests.get('https://httpbin.org/delay/3', timeout=2)
#    raise ReadTimeout(e, request=request)
# ReadTimeout: HTTPSConnectionPool(host='httpbin.org', port=443): Read timed out. (read timeout=2)

if 1 == 0:
    print(dir(r))
    print(help(r))
    print(r.headers)

# formed based vs basic Authentication

