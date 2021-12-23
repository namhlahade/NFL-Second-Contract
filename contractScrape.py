import pandas as pd
import math
from pandas.io.formats.format import common_docstring
from pandas.io.parsers import read_csv
import requests
import csv
from bs4 import BeautifulSoup

URL = 'https://overthecap.com/position/quarterback/'
qbURL = 'https://overthecap.com'
year = 1994
contractDict = {}
while (year <=2031):
    newURL = URL + str(year) + '/'
    year = year + 1
    
    page = requests.get(newURL)
    soup = BeautifulSoup(page.content, "html.parser")
    table = soup.find('table', {'class':'position-table sortable'})
    body = table.find('tbody')
    tr = body.find_all('tr')
    flag = 0
    for tag in tr:
        td = tag.find('td')
        a = td.find('a')
        try:
            qbLink = qbURL + a['href'] + '#contract-history'
            
            newPage = requests.get(qbLink)
            newSoup = BeautifulSoup(newPage.content, "html.parser")
            name = newSoup.find('h3')

            name = name.text.strip()
            table = newSoup.find('table', {'class':'contract salary-cap-history player-new'})
            tbody = table.find('tbody')
        except AttributeError:
            qbLink = qbURL + a['href']
            newPage = requests.get(qbLink)
            newSoup = BeautifulSoup(newPage.content, "html.parser")
            name = newSoup.find('h3')
            name = name.text.strip()
            table = newSoup.find('table', {'class': 'contract current-contract player-new'})
            tbody = table.find('tbody')
            flag = 1
        if flag == 0:
            rows = tbody.find_all('tr')
            headstart = table.find('thead')
            head = headstart.find_all('th')
            head = [x.text.strip() for x in head]
            head.append('Name')
            for row in rows:
                cols = row.find_all('td')
                cols = [x.text.strip() for x in cols]
                cols.append(name)
                col = list(zip(head, cols))
                if name in contractDict.keys():
                    contractDict[name].append(col)
                else:
                    contractDict[name] =[col]
        flag = 0
#print(contractDict)
with open('/Users/namhlahade/Documents/GitHub/NFL-Second-Contract/qbSeasonContracts.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    for name in contractDict.keys():
        count = 0
        oneYear = contractDict[name]
        header = []
        totalData = []
        for breakDown in oneYear:
            lineData = []
            for item in breakDown:
                x, data = item
                if count == 0:
                    header.append(x)
                lineData.append(data)
            totalData.append(lineData)
            count = 1
        print('header')
        print(header)
        print('data')
        writer.writerow(header)
        x = 0
        dict = {}
        for d in totalData:
            if d[0] not in dict.keys():
                print(d)
                writer.writerow(d)
                dict[d[0]] = [d]