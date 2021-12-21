import pandas as pd
import math
from pandas.io.formats.format import common_docstring
import requests
import csv
from bs4 import BeautifulSoup

linksCSV = pd.read_csv('/Users/namhlahade/Documents/GitHub/NFL-Second-Contract/relevantLinks.csv')
rookieQBCSV = pd.read_csv('/Users/namhlahade/Documents/GitHub/NFL-Second-Contract/rookieQBs.csv')
names = linksCSV['Name'].tolist()
links = linksCSV['Link'].tolist()
startYr = rookieQBCSV['Year'].tolist()
rookieNames = rookieQBCSV['Name'].tolist()

combinedList = zip(rookieNames, startYr)
tempDictionary = dict(combinedList)

zip_iterator = zip(names, links)
qbDictionary = dict(zip_iterator)

for name in qbDictionary:
    qbDictionary[name] = [name, tempDictionary[name], qbDictionary[name]]

header = ['Name','Year', 'Draft_Yr', 'Age','Tm','Pos','No.','G'	,'S','QBrec','Cmp','Att','Cmp%'	,'Yds','TD','TD%','Int','Int%','1D','Lng','Y/A','AY/A','Y/C','Y/G','Rate','QBR','Sk','Yds','Sk%','NY/A','ANY/A','4QC','GWD','AV']
with open('/Users/namhlahade/Documents/GitHub/NFL-Second-Contract/relevantQBstats.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for name in qbDictionary.keys():
        URL = qbDictionary[name][2]
        print(URL)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")

        if soup.find('table', {'id': 'passing'}):
            table = soup.find('table', {'id': 'passing'})
            rows = table.find_all('tr', {'class': 'full_table'})
            rookieYears = 0
            count = 0
            for row in rows:
                head = row.find('th')
                head = [y.text.strip() for y in head]
                cols = row.find_all('td')
                cols = [x.text.strip() for x in cols]
                cols.insert(0, name)
                cols.insert(1, head[0])
                if count <= 3:
                    cols.insert(2, 'Rookie Deal')
                    count = count + 1
                else:
                    cols.insert(2, 'Veteran Deal')
                print(cols)
                writer.writerow(cols)
