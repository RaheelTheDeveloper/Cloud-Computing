#!flask/bin/python
from flask import Flask, jsonify
import subprocess
import sys
import json
import re
import os
from tasks import CountWords

app = Flask(__name__)


@app.route('/tweets/', methods=['GET'])

def totalCount():
    totalWordCount = [["han",0], ["hon",0], ["den",0], ["det",0], ["denna",0], ["denne",0],["hen",0]]
    totalWordCountString = " "
    path = "/home/ubuntu/data/"
    dir_list = os.listdir(path)

    for dir in dir_list:
        result = CountWords.delay(dir)
        result.ready()
        result = result.get(timeout=1)

        for res, res1 in result:
            if(res == "han"):
                totalWordCount[0][1] = totalWordCount[0][1] + res1
            elif(res == "hon"):
                totalWordCount[1][1] = totalWordCount[1][1] + res1
            elif(res == "den"):
                totalWordCount[2][1] = totalWordCount[2][1] + res1
            elif(res == "det"):
                totalWordCount[3][1] = totalWordCount[3][1] + res1
            elif(res == "denna"):
                totalWordCount[4][1] = totalWordCount[4][1] + res1
            elif(res == "denne"):
                totalWordCount[5][1] = totalWordCount[5][1] + res1
            elif(res == "hen"):
                totalWordCount[6][1] = totalWordCount[6][1] + res1


    wordCountTostr = ' '.join([str(elem) for elem in totalWordCount])
    return wordCountTostr

if __name__ == '__main__':

    app.run(host='0.0.0.0',debug=True)
