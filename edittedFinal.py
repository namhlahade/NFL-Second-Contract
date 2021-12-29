from typing import FrozenSet, final
import pandas as pd
import math
from pandas.io.formats.format import common_docstring
from pandas.io.parsers import read_csv
import requests
import csv
from csv import writer
from csv import reader
from bs4 import BeautifulSoup



def merge(list1, list2):  
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
    return merged_list

def merge2(list1, list2, list3):
    merged_list = [(list1[i], list2[i], list3[i]) for i in range(0, len(list1))]
    return merged_list
    
def merge3(list1, list2, list3, list4, list5):
    merged_list = [(list1[i], list2[i], list3[i], list4[i], list5[i]) for i in range(0, len(list1))]
    return merged_list


dataPoints = pd.read_csv('/Users/namhlahade/Documents/GitHub/NFL-Second-Contract/finalData.csv')
everything = pd.read_csv('/Users/namhlahade/Documents/GitHub/NFL-Second-Contract/qbSeasonContracts.csv')
extensions = pd.read_csv('/Users/namhlahade/Documents/GitHub/NFL-Second-Contract/extensions.csv')
nameSeason = everything['Name'].tolist()
teamSeason = everything['Team'].tolist()
yearSeason = everything['Year'].tolist()
names = dataPoints['Name'].tolist()
years = dataPoints['Year'].tolist()
extName = extensions['Name'].tolist()
extTeam = extensions['Team'].tolist()
extContract = extensions['Contract Type'].tolist()
extYear = extensions['Year Signed'].tolist()
extLength = extensions['Yrs'].tolist()


newList = merge(names, years)
newTupleEverything = merge2(nameSeason, teamSeason, yearSeason)
newTupleExtensions = merge3(extName, extTeam, extContract, extYear, extLength)

teamNamesDict = {}
for element in newTupleEverything:
    name, team, year = element
    newKey = name + " " + team
    teamNamesDict[newKey] = year
# 3 means that they are too young, 1 means that they lasted more than 4 years after contract extension,  0 means they didnt last more than 4 years after contract extension. 2 means they still need to be evaluated
nameExtensionDict = {}
for element in newTupleExtensions:
    name, team, contract, year, length = element
    if (contract == 'Extension' and length >= 4) or (contract == 'Other' and length >= 4) or (contract == 'Franchise' and length >= 4) or (contract == 'UFA' and length >= 4):
        if name not in nameExtensionDict.keys():
            nameExtensionDict[name] = [team, year, 2]
    elif contract == 'Drafted' and year >= 2019:
        nameExtensionDict[name] = [team, year, 3]
nameExtensionDict['Jared Goff'] = ['Rams', 2019, 2]
nameExtensionDict['Sam Darnold'] = ['Panthers', 2021, 0]
nameExtensionDict['Josh Rosen'] = ['49ers', 2021, 0]
nameExtensionDict['Baker Mayfield'] = ['Browns', 2021, 0]
nameExtensionDict['Kyle Lauletta'] = ['Browns', 2021, 0]
nameExtensionDict['Mitchell Trubisky'] = ['Bills', 2021, 0]
nameExtensionDict['DeShone Kizer'] = ['Titans', 2021, 0]
nameExtensionDict['C.J. Beathard'] = ['49ers', 2021, 0]
nameExtensionDict['Mark Brunell'] = ['Packers', 2011, 0]
nameExtensionDict['Rob Johnson'] = ['Bills', 1995, 0]




for element in names:
    if element not in nameExtensionDict.keys():
        for e in newTupleExtensions:
            if e[0] == element:
                nameExtensionDict[e[0]] = [e[1], e[3], 0]

namesAlreadyDone = {}
for name in nameExtensionDict.keys():
    if nameExtensionDict[name][2] == 2:
        for element in newTupleExtensions:
            if (element[2] == 'Extension' and element[4] >= 4) or (element[2] == 'Other'  and element[4] >= 4) or (element[2] == 'Franchise' and element[4] >= 4) or (element[2] == 'UFA' and element[4] >= 4):
                if element[0] not in namesAlreadyDone.keys():
                    namesAlreadyDone[element[0]] = [element[1], element[2], element[3], element[4]]

for name in namesAlreadyDone.keys():
    for element in newTupleEverything:
        if element[0] == name and namesAlreadyDone[name][2] <= 2017 and ((namesAlreadyDone[name][2] + 4) <= element[2] and namesAlreadyDone[name][0] == element[1]):
            nameExtensionDict[name] = [element[0], element[2], 1]
            print(name, namesAlreadyDone[name][0], element[1])
nameExtensionDict['Colin Kaepernick'] = ['49ers', 2014, 1]
nameExtensionDict['Andrew Luck'] = ['Colts', 2016, 1]
nameExtensionDict['Kirk Cousins'] = ['Vikings', 2018, 1]
nameExtensionDict['Jimmy Garoppolo'] = ['49ers', 2018, 1]
nameExtensionDict['Dak Prescott'] = ['Cowboys', 2021, 1]
nameExtensionDict['Patrick Mahomes'] = ['Chiefs', 2020, 1]
nameExtensionDict['Deshaun Watson'] = ['Texans', 2020, 1]
nameExtensionDict['Josh Allen'] = ['Bills', 2021, 1]


for name in nameExtensionDict.keys():
    if nameExtensionDict[name][2] == 2:
        for element in newTupleExtensions:
            nam, team, contract, year, length = element
            if nam == name:
                nameExtensionDict[name] = [team, year, 0]

nameExtensionDict['Kurt Warner'] = ['Rams', 1998, 1]
nameExtensionDict['Matt Schaub'] = ['Texans', 2012, 0]
nameExtensionDict['Shuan Hill'] = ['Vikings', 2005, 0]
nameExtensionDict['Matt Cassel'] = ['Chiefs', 2012, 0]
nameExtensionDict['Ryan Fitzpatrick'] = ['Bills', 2009, 0]
nameExtensionDict['Mark Sanchez'] = ['Jets', 2012, 0]
nameExtensionDict['Chase Daniel'] = ['Bears', 2012, 0]
nameExtensionDict['Colt McCoy'] = ['Texans', 2012, 0]
nameExtensionDict['Tyrod Taylor'] = ['Texans', 2012, 0]
nameExtensionDict['Ryan Tannehill'] = ['Texans', 2012, 0]
nameExtensionDict['Kirk Cousins'] = ['Texans', 2012, 0]
nameExtensionDict['Mike Glennon'] = ['Texans', 2012, 0]
nameExtensionDict['Jimmy Garoppolo'] = ['Texans', 2012, 0]
nameExtensionDict['Daniel Jones'] = ['Texans', 2012, 0]
nameExtensionDict['Dwayne Haskins'] = ['Texans', 2012, 0]
nameExtensionDict['Drew Lock'] = ['Texans', 2012, 0]
nameExtensionDict['Will Grier'] = ['Texans', 2012, 0]
nameExtensionDict['Ryan Finley'] = ['Texans', 2012, 0]
nameExtensionDict['Jarrett Stidham'] = ['Texans', 2012, 0]
nameExtensionDict['Easton Stick'] = ['Texans', 2012, 0]
nameExtensionDict['Gardner Minshew'] = ['Texans', 2012, 0]
nameExtensionDict['Jacob Eason'] = ['Texans', 2012, 0]
nameExtensionDict['Jake Fromm'] = ['Texans', 2012, 0]
nameExtensionDict['Jake Luton'] = ['Texans', 2012, 0]
nameExtensionDict['Ben DiNucci'] = ['Texans', 2012, 0]
nameExtensionDict['Nate Stanley'] = ['Texans', 2012, 0]
nameExtensionDict['Tommy Stevens'] = ['Texans', 2012, 0]
print(nameExtensionDict)

newList = []
for name in names:
    if name in nameExtensionDict.keys():
        newList.append(nameExtensionDict[name][2])
print(len(newList))
print(len(names))


with open('/Users/namhlahade/Documents/GitHub/NFL-Second-Contract/finalData.csv', 'r') as read_obj, \
        open('/Users/namhlahade/Documents/GitHub/NFL-Second-Contract/actualfinalData.csv', 'w', newline='') as write_obj:
    # Create a csv.reader object from the input file object
    csv_reader = reader(read_obj)
    # Create a csv.writer object from the output file object
    csv_writer = writer(write_obj)

    flag = False
    i = 0
    for row in csv_reader:
        if flag == True:
            row.append(newList[i])
            i = i + 1
        csv_writer.writerow(row)
        flag = True