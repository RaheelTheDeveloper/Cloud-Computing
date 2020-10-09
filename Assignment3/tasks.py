import sys
import json
import re
from celery import Celery

broker_url = 'amqp://raheel:raheelpassword@192.168.2.94:5672/raheelhost'
app = Celery('tasks', backend='rpc://', broker=broker_url)

@app.task
def CountWords(fileToProcess):
 uniqueCount = 0
 wordsToShow = [["han",0], ["hon",0], ["den",0], ["det",0], ["denna",0], ["denne",0],["hen",0]]

 file1 = open('/home/ubuntu/data/' + fileToProcess, 'r')
 for line in file1:

     line = line.strip()
     if len(line) == 0:
      continue

     myJson = json.loads(line)
     #print('%s\t%s' % ("TOTAL", 1))
     if 'retweeted_status' not in myJson:
      uniqueCount = uniqueCount + 1
      #print('%s\t%s' % ("UNIQUE", 1))
      text = myJson['text'].lower()
      textArray = text.split(" ")

      for word in wordsToShow:
       if textArray.count(word[0]) > 0:
        word[1] = word[1] + 1
        #print(wordsToShow)

 return wordsToShow
#CountWords("05cb5036-2170-401b-947d-68f9191b21c6")
