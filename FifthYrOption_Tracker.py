from typing import TypedDict
import pandas as pd
import math
from pandas.io.formats.format import common_docstring
from pandas.io.parsers import read_csv
import requests
import csv
from bs4 import BeautifulSoup
import numpy

qbData = pd.read_csv('/Users/namhlahade/Documents/GitHub/NFL-Second-Contract/relevantQBstats.csv')
names = qbData['Name'].tolist()
year = qbData['Year'].tolist()
dealType = qbData['Draft_Yr'].tolist()
gamesStarted = qbData['S'].tolist()
record = qbData['QBrec'].tolist()
count = 0
for yr in record:
    if type(yr) == float:
        record[count] = '0-0-0'
    count = count + 1
completionPercentage = qbData['Cmp%'].tolist() #If completion percentage is nan, this means that 0 passes were thrown and completed
yds = qbData['Yds'].tolist()
touchdown = qbData['TD'].tolist()
int = qbData['Int'].tolist()
tdPercentage = qbData['TD%'].tolist() #If td percentage is nan, this means that 0 passes were thrown and completed
intPercentage = qbData['Int%'].tolist() #If int percentage is nan, this means that 0 passes were thrown and completed
firstdownsPassing = qbData['1D'].tolist()
adjustedYperA = qbData['AY/A'].tolist() #If adjusted yards per attemp is nan, this means that 0 passes were thrown and completed
yardspercomp = qbData['Y/C'].tolist() #If yards per completion is nan, this means that 0 passes were thrown and completed
yardspergame = qbData['Y/G'].tolist()
qbr = qbData['QBR'].tolist() #If QBR is nan, this means that 0 passes were thrown and completed
sackPercentage = qbData['Sk%'].tolist() #If Sack Percentage is nan, this means that 0 passes were thrown and completed
comebacks = qbData['4QC'].tolist()

newList = [names, year, dealType, gamesStarted, record, completionPercentage, yds, touchdown, int, tdPercentage, intPercentage, firstdownsPassing, adjustedYperA, yardspercomp, yardspergame, qbr, sackPercentage, comebacks]

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