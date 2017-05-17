#!/usr/bin/python
import cgi
import cgitb
import random
import sys
import json
cgitb.enable()

try:
	dataFile=open('history.txt')
	data=json.load(dataFile)
	dataFile.close()
except ValueError:
	data={"rounds":[]}
except IOError as err:
	print('FILE ERROR'+ str(err))	

myjson=json.load(sys.stdin)
#myjson={'param':{'name':'Alar', "date":'2016-11-05'}}
searchName=myjson['param']['name']
searchDate=myjson['param']['date']

if searchName!='' and searchDate=='':
  myData={"rounds":[]}
  for item in data['rounds']:
    if searchName in item['playername']:
        myData['rounds'].append(item)
  response=myData
elif searchName=='' and searchDate!='':
  myData={"rounds":[]}
  for item in data['rounds']:
    if searchDate in item['time']:
        myData['rounds'].append(item)
  response=myData
elif searchName!='' and searchDate!='':
  myData={"rounds":[]}
  for item in data['rounds']:
    if searchDate in item['time'] and searchName in item['playername']:
      myData['rounds'].append(item)
    response=myData
else:
  response=data


print 'Content-Type: application/json\n\n'
json.dump(response, sys.stdout)







