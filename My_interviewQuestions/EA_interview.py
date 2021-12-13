# import math
#
# Val = 3
#
# sqroot = math.sqrt(Val)
# #print((sqroot ** 2))
#
# Exponential = math.exp(Val)
# #print(power)
#
# factVal = math.factorial(Val)
# #print(factVal)
#
# SinVal = math.sin(3.14)
# print(SinVal)
# floorVal = math.floor(SinVal)
# CeilVal = math.ceil(SinVal)
# print(floorVal)
# print(CeilVal)

# import numpy as np
#
# a = np.array([1,2,3])
# #print(a)
# b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
# #print(b)
# print(a.ndim)
# print(b.ndim)
# print(a.shape)
# print(b.size)

# import random
# # list = [1,2,3]
# # # value = random.randint(1,10)
# # value = random.choices(list, weights=[18,18,2], k=10)
# # print(value)
# deck = list(range(1,53))
# random.shuffle(deck)
# hand = random.sample(deck, k=5)
# print(hand)


import os
from datetime import datetime

print((os.getcwd()))
#os.mkdir()
#os.makedirs('xyz\yzx')
#os.removedirs('xyz\yzx')
# os.chdir('C:\')
#print(os.listdir())
modifiedtime = os.stat('EA_interview.py').st_mtime
print(datetime.fromtimestamp(modifiedtime))

# for dirpath, dirnames, filenames in os.walk(os.getcwd()):
#     print(dirpath,dirnames,filenames)
#
# print(os.environ.get('HOME'))
#
# os.path.join('HOME' 'test')
#
# print(os.path.exists('/tmp/xyz'))
#
# print(os.path.splitext('text.txt'))

# import sys
# #print(sys.path)
# # sys.stderr.write('test\n')
# # sys.stderr.flush()
# # sys.stdout.write('this is sysout\n')
# print(sys.argv)


import requests

r = requests.get('https://imgs.xkcd.com/comics/python.png')
#response = r.status_code()
#print(r.content)
print(r.headers)
# with open('comic.png', 'wb') as f:
#     f.write(r.content)

#args = {'page': 2, 'count': 25}
args = {'username': 'corey', 'password': 'testing'}
#r = requests.get('https://httpbin.org/get', params=args)
r = requests.post('https://httpbin.org/post', data=args)

r_dict = r.json()
print(r_dict['form'])


names = ['Corey', 'Fayaz', 'Dave']

for index, name in enumerate(names, start=1):
    print(index, name)

# names = ['Peter', 'clake', 'wade']
# heros = ['spider', 'super', 'deadpool']
#
# for name, super in zip(names, heros):
#     print(f'{name} is actually {super}')
#
# a,b, *c = [1,2,3,4,5,6]
# print(a)
# print(b)
# print(c)

# print(datetime.today())

import  json

data = json.loads(string)




























































