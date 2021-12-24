from typing import TypedDict, final
import pandas as pd
import math
from pandas.io.formats.format import common_docstring
from pandas.io.parsers import read_csv
import requests
import csv
from bs4 import BeautifulSoup
import numpy
from rookieYears import dealLengthDict

qbData = pd.read_csv('/Users/namhlahade/Documents/GitHub/NFL-Second-Contract/relevantQBstats.csv')
names = qbData['Name'].tolist()
year = qbData['Year'].tolist()
dealType = qbData['Draft_Yr'].tolist()
gamesStarted = qbData['S'].tolist()
record = qbData['QBrec'].tolist()
contract = pd.read_csv('/Users/namhlahade/Documents/GitHub/NFL-Second-Contract/qbSeasonContracts.csv')
count = 0
for yr in record:
    if type(yr) == float:
        record[count] = '0-0-0'
    count = count + 1
completionPercentage = qbData['Cmp%'].tolist() #If completion percentage is nan, this means that 0 passes were thrown and completed
yds = qbData['Yds'].tolist()
touchdown = qbData['TD'].tolist()
interception = qbData['Int'].tolist()
tdPercentage = qbData['TD%'].tolist() #If td percentage is nan, this means that 0 passes were thrown and completed
intPercentage = qbData['Int%'].tolist() #If interception percentage is nan, this means that 0 passes were thrown and completed
firstdownsPassing = qbData['1D'].tolist()
adjustedYperA = qbData['AY/A'].tolist() #If adjusted yards per attemp is nan, this means that 0 passes were thrown and completed
yardspercomp = qbData['Y/C'].tolist() #If yards per completion is nan, this means that 0 passes were thrown and completed
yardspergame = qbData['Y/G'].tolist()
qbr = qbData['QBR'].tolist() #If QBR is nan, this means that 0 passes were thrown and completed
sackPercentage = qbData['Sk%'].tolist() #If Sack Percentage is nan, this means that 0 passes were thrown and completed
comebacks = qbData['4QC'].tolist()

newList = [names, year, dealType, gamesStarted, record, completionPercentage, yds, touchdown, interception, tdPercentage, intPercentage, firstdownsPassing, adjustedYperA, yardspercomp, yardspergame, qbr, sackPercentage, comebacks]

count = 0
for fd in newList[11]:
   if math.isnan(fd):
       newList[11][count] = 0.0
   count = count + 1
count = 0
for yg in newList[14]:
   if math.isnan(yg):
       newList[14][count] = 0.0
   count = count + 1
count = 0
for comeback in newList[17]:
   if math.isnan(comeback):
       newList[17][count] = 0.0
   count = count + 1

a = numpy.array(newList)
c = numpy.array([])
y = numpy.asarray(a[1], dtype=numpy.float64, order='C')
for x in range(len(newList[1])):
    if newList[1][x] >= 1994:
        b = numpy.array([])
        for y in range(len(a)):
            b = numpy.append(b, a[y][x])
        c = numpy.append(c, b, axis=0)

arr_2d = numpy.reshape(c, (1789, 18))
finalArray = numpy.ndarray.tolist(arr_2d)
qbDict = {}
for element in finalArray:
    if element[0] not in qbDict.keys():
        b = element[:1]
        c = b[0]
        d = element[1:]
        e = d[3].split('-')
        d[3] = e[0]
        d.append(1)
        qbDict[c] = d
    elif element[0] in qbDict.keys():
        number = qbDict[element[0]][17]
        avGames = ((float(qbDict[element[0]][2]))*number + float(element[3]))/(number + 1)
        qbDict[element[0]][2] = avGames #averaging the games started
        avWon = element[4]
        won = avWon.split('-')
        wonAvg = ((float(qbDict[element[0]][3]))*number + float(won[0]))/(number + 1)
        qbDict[element[0]][3] = wonAvg
        avCompPer = ((float(qbDict[element[0]][4]))*number + float(element[5]))/(number + 1)
        qbDict[element[0]][4] = avCompPer #averaging completion percentage
        ydsAvg = ((float(qbDict[element[0]][5]))*number + float(element[6]))/(number + 1)
        qbDict[element[0]][5] = ydsAvg #averaging the yds
        tdAvg = ((float(qbDict[element[0]][6]))*number + float(element[7]))/(number + 1)
        qbDict[element[0]][6] = tdAvg #averaging the touchdowns
        intAvg = ((float(qbDict[element[0]][7]))*number + float(element[8]))/(number + 1)
        qbDict[element[0]][7] = intAvg #averaging the floaterceptions
        tdper = ((float(qbDict[element[0]][8]))*number + float(element[9]))/(number + 1)
        qbDict[element[0]][8] = tdper #averaging the touchdown percentages
        intPer = ((float(qbDict[element[0]][9]))*number + float(element[10]))/(number + 1)
        qbDict[element[0]][9] = intPer #averaging the floaterception percentages
        fdPass = ((float(qbDict[element[0]][10]))*number + float(element[11]))/(number + 1)
        qbDict[element[0]][10] = fdPass #averaging the first down passings
        ayoa = ((float(qbDict[element[0]][11]))*number + float(element[12]))/(number + 1)
        qbDict[element[0]][11] = ayoa
        yPerComp = ((float(qbDict[element[0]][12]))*number + float(element[13]))/(number + 1)
        qbDict[element[0]][12] = yPerComp
        yPerGame = ((float(qbDict[element[0]][13]))*number + float(element[14]))/(number + 1)
        qbDict[element[0]][13] = yPerGame
        quarterbackR = ((float(qbDict[element[0]][14]))*number + float(element[15]))/(number + 1)
        qbDict[element[0]][14] = quarterbackR
        sackPer = ((float(qbDict[element[0]][15]))*number + float(element[16]))/(number + 1)
        qbDict[element[0]][15] = sackPer
        cBack = ((float(qbDict[element[0]][16]))*number + float(element[17]))/(number + 1)
        qbDict[element[0]][16] = cBack

        qbDict[element[0]][17] = qbDict[element[0]][17] + 1

for name in qbDict.keys():
    if qbDict[name][17] > 4:
        qbDict[name][1] = 'Veteran Deal'

qbDictRookie = {}
for element in finalArray:
   if element[0] not in qbDictRookie.keys():
       b = element[:1]
       c = b[0]
       d = element[1:]
       e = d[3].split('-')
       d[3] = e[0]
       d.append(1)
       qbDictRookie[c] = d
  
   elif element[0] in qbDictRookie.keys() and (qbDictRookie[element[0]][17] != 4):
       number = qbDictRookie[element[0]][17]
       avGames = ((float(qbDictRookie[element[0]][2]))*number + float(element[3]))/(number + 1)
       qbDictRookie[element[0]][2] = avGames #averaging the games started
       avWon = element[4]
       won = avWon.split('-')
       wonAvg = ((float(qbDictRookie[element[0]][3]))*number + float(won[0]))/(number + 1)
       qbDictRookie[element[0]][3] = wonAvg
       avCompPer = ((float(qbDictRookie[element[0]][4]))*number + float(element[5]))/(number + 1)
       qbDictRookie[element[0]][4] = avCompPer #averaging completion percentage
       ydsAvg = ((float(qbDictRookie[element[0]][5]))*number + float(element[6]))/(number + 1)
       qbDictRookie[element[0]][5] = ydsAvg #averaging the yds
       tdAvg = ((float(qbDictRookie[element[0]][6]))*number + float(element[7]))/(number + 1)
       qbDictRookie[element[0]][6] = tdAvg #averaging the touchdowns
       intAvg = ((float(qbDictRookie[element[0]][7]))*number + float(element[8]))/(number + 1)
       qbDictRookie[element[0]][7] = intAvg #averaging the floaterceptions
       tdper = ((float(qbDictRookie[element[0]][8]))*number + float(element[9]))/(number + 1)
       qbDictRookie[element[0]][8] = tdper #averaging the touchdown percentages
       intPer = ((float(qbDictRookie[element[0]][9]))*number + float(element[10]))/(number + 1)
       qbDictRookie[element[0]][9] = intPer #averaging the floaterception percentages
       fdPass = ((float(qbDictRookie[element[0]][10]))*number + float(element[11]))/(number + 1)
       qbDictRookie[element[0]][10] = fdPass #averaging the first down passings
       ayoa = ((float(qbDictRookie[element[0]][11]))*number + float(element[12]))/(number + 1)
       qbDictRookie[element[0]][11] = ayoa
       yPerComp = ((float(qbDictRookie[element[0]][12]))*number + float(element[13]))/(number + 1)
       qbDictRookie[element[0]][12] = yPerComp
       yPerGame = ((float(qbDictRookie[element[0]][13]))*number + float(element[14]))/(number + 1)
       qbDictRookie[element[0]][13] = yPerGame
       quarterbackR = ((float(qbDictRookie[element[0]][14]))*number + float(element[15]))/(number + 1)
       qbDictRookie[element[0]][14] = quarterbackR
       sackPer = ((float(qbDictRookie[element[0]][15]))*number + float(element[16]))/(number + 1)
       qbDictRookie[element[0]][15] = sackPer
       cBack = ((float(qbDictRookie[element[0]][16]))*number + float(element[17]))/(number + 1)
       qbDictRookie[element[0]][16] = cBack
 
       qbDictRookie[element[0]][17] = qbDictRookie[element[0]][17] + 1

quarterBackDict = {}
for name in qbDictRookie.keys():
    if name in dealLengthDict.keys():
        newt = qbDictRookie[name] + dealLengthDict[name]
        quarterBackDict[name] = newt
print(quarterBackDict)
    
