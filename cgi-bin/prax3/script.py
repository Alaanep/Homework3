#!/usr/bin/python
import cgi
import cgitb
import random
import sys
import json
import datetime
cgitb.enable()
myData={}

#player class to create user and computer objects
class Player:
	def __init__(self, a_move='', a_name='', a_moves=[], a_score=0, a_round=0, a_result='', a_time='', a_dict=''):
		#the code to initialize  a player object
		self.move=a_move
		self.name=a_name
		self.score=a_score
		self.round=a_round
		self.result=a_result
		self.time=a_time
		self.moves=a_moves

	#add round
	def addRound(self):
		self.round+=1
		
	#add round
	def addScore(self):
		self.score+=1

	#get score
	def getScore(self):
		return self.score
		
	#get rounds
	def getRounds(self):
		return self.round
	
	#get player name	
	def getUserName(self):
		return self.name


user=Player(a_name='player')
computer=Player(a_name='computer')



#computer makes a choice
def computerChoice():
	computerMove=random.randint(1,3)
	if computerMove==1:
		computerMove='rock'
	elif computerMove==2:
		computerMove='scissors'
	elif computerMove==3:
		computerMove='paper'
	

	#todo create computer strategy when dictionary is ready
	dataForStrategy=readFromFile('165332CTF.txt') #session data
	if dataForStrategy=="":
		dataForStrategy={"rounds":[]}
	if len(dataForStrategy['rounds'])>3:
		if user.move == dataForStrategy['rounds'][-1]['usermove'] and dataForStrategy['rounds'][-1]['usermove'] == dataForStrategy['rounds'][-2]['usermove'] and dataForStrategy['rounds'][-2]['usermove'] == dataForStrategy['rounds'][-3]['usermove']:
			if user.move=='rock':
				computermove='paper'
				return computermove
			elif user.move=='scissors':
				computermove='rock'
				return computermove
			elif user.move=='paper':
				computermove='scissors'
				return computermove
	return computerMove



#compare function will determine who won and update score accordingly. Return string with winner name and winner weapon
def compare(human, cpu):
	if human==cpu:
		return 'TIE!'
	elif human=='rock':
		if cpu=='scissors':
			user.addScore()
			return str(user.getUserName())+' wins with rock!'
		elif cpu=='paper':
			computer.addScore()
			return str(computer.getUserName())+' wins with paper!'
	elif human=='paper':
		if cpu=='rock':
			user.addScore()
			return str(user.getUserName())+' wins with paper!'
		elif cpu=='scissors':
			computer.addScore()
			return str(computer.getUserName())+' wins with scissors!'
	elif human=='scissors':
		if cpu=='rock':
			computer.addScore()
			return str(computer.getUserName())+' wins with rock!'
		elif cpu=='paper':
			user.addScore()
			return str(user.getUserName())+' wins with scissors!'


#write JSON data to '165332CTF.txt' file
def writeToFile(data, fileName):
	try:
		with open(fileName, 'w') as dataFile:
			json.dump(data, dataFile, indent=4, sort_keys=True, separators=(',', ':'))

	except IOError as err:
		print('FILE ERROR'+ str(err))

def readFromFile(fileName):
	try:
		dataFile=open(fileName)
		data=json.load(dataFile)
		dataFile.close()
	except ValueError:
		data=""
	except IOError as err:
		print('FILE ERROR'+ str(err))	
	return data

myjson=json.load(sys.stdin)
user.move=myjson['param']['usermove']
user.name=myjson['param']['username']

computer.move=computerChoice()
myData=readFromFile('165332CTF.txt') #session data
myHistory=readFromFile('history.txt') #history data
if myData=="":
	myData={"rounds":[]}
	user.round=0
	user.score=0
	computer.score=0
else:
	user.round=myData['rounds'][-1]['userround']
	user.score=myData['rounds'][-1]['userscore']
	computer.score=myData['rounds'][-1]['computerscore']
if myHistory=="":
	myHistory={"rounds":[]}
	user.round=0
	user.score=0
	computer.score=0

user.result=compare(user.move, computer.move)
user.addRound()
user.time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
roundData={'playername':user.name, 'userround':user.round,'usermove': user.move, 'computermove':computer.move, 'result':user.result, 'userscore':user.score, 'computerscore':computer.score, 'time':user.time }

myData["rounds"].append(roundData) #add roundData to sessionData
myHistory["rounds"].append(roundData)#add roundData to historyData
writeToFile(myData, '165332CTF.txt') 
writeToFile(myHistory, 'history.txt')

print 'Content-Type: application/json\n\n'
json.dump(roundData, sys.stdout)