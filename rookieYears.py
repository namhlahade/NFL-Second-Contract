from typing import TypedDict, final
import pandas as pd
import math
from pandas.io.formats.format import common_docstring
from pandas.io.parsers import read_csv
import requests
import csv
from bs4 import BeautifulSoup

def merge(list1, list2, list3, list4):
      
    merged_list = [(list1[i], list2[i], list3[i], list4[i]) for i in range(0, len(list1))]
    return merged_list

extensions = pd.read_csv('/Users/namhlahade/Documents/GitHub/NFL-Second-Contract/extensions.csv')
names = extensions['Name'].tolist()
contractStatus = extensions['Contract Type'].tolist()
yearSigned = extensions['Year Signed'].tolist()
combined = merge(names, contractStatus, yearSigned, yearSigned)

dealLengthDict = {}
for element in combined:
    name, contract, year, yearStarted = element
    if name not in dealLengthDict.keys():
        dealLengthDict[name] = [contract, year, 0, 0, yearStarted]
    if name in dealLengthDict.keys() and dealLengthDict[name][3] == 0:
        if contract == 'Other' or contract == 'Extension':
            dealLengthDict[name][3] = 1
            dealLengthDict[name][2] = year - dealLengthDict[name][1]
            dealLengthDict[name][1] = year
            dealLengthDict[name][0] = contract

for name in list(dealLengthDict.keys()):
    if dealLengthDict[name][4] < 1994:
        del(dealLengthDict[name])