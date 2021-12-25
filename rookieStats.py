from os import stat
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
from CombiningCSV import thisIsFinal

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

statsDict = {}
for listElement in finalArray:
    if listElement[0] in thisIsFinal.keys():
        for statRow in thisIsFinal[listElement[0]]:
            if int(listElement[1]) == statRow[1] and listElement[0] not in statsDict.keys():
                statsDict[listElement[0]] = []
                statsDict[listElement[0]].append(listElement)
                statsDict[listElement[0]].append(statRow)
            elif int(listElement[1]) == statRow[1] and listElement[0] in statsDict.keys():
                statsDict[listElement[0]].append(listElement)
                statsDict[listElement[0]].append(statRow)

header = ['Name', 'Year', 'Deal Type', 'Games Played', 'Record', 'Completion Percentage', 'Yards', 'Touchdowns', 'Interceptions', 'Touchdown Percentage', 'Interception Percentage', 'First Downs Passing', 'Adjusted Yards per Attempt', 'Yards per Completion', 'Yards per Game', 'QBR' , 'Sack Percentage', 'Comebacks', 'Team', 'Year', 'Base Salary', 'Prorated Bonus', 'Roster Bonus', 'Cap Number', 'Cap Percentage', 'Cash Paid', 'Guaranteed Salary', 'Other Bonus', 'Workout Bonus', 'Per Game Roster Bonus']
with open('/Users/namhlahade/Documents/GitHub/NFL-Second-Contract/finalData.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for name in statsDict.keys():
        statsDict[name][0].pop(0)
        newList = [name] + statsDict[name][0] + statsDict[name][1]
        writer.writerow(newList)

