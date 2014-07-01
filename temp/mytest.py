# coding: utf-8

from sphinxapi import *
import sys


cl = SphinxClient()
cl.SetServer('127.0.0.1', 9312)
res = cl.Query('')

if not res:
    SearchResult = 'Поиск не дал результатов. Пожалуйста, попробуйте поменять условия вашего запроса'
    sr_id = 0

data = {}
if res.has_key('matches'):
    n = 1
    sr_id = 1
    for match in res['matches']:
        data[n] = {'id' : match['id'] , 'row_type' : match['attrs']['row_type']}
        n += 1

datar1 = []
#datar1 = ''
datar2 = []
i = 0
for key in data:
    a = data[key]['row_type']
    if a == 1:
        datar1.insert(i, data[key]['id'])
    elif a == 2:
        datar2.insert(i, data[key]['id'])
    i += 1

if len(datar1) == 1:
    datar1.append(0)
if len(datar2) == 1:
    datar2.append(0)

print (datar1)
print (len(datar1))
print (datar2)
print (len(datar2))
if sr_id == 0:
    print (SearchResult)



