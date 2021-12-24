from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

URL = 'https://overthecap.com/position/quarterback/'
qbURL = 'https://overthecap.com'
year = 1994
contractDict = {}
header = ['Team', 'Contract Type', 'Status', 'Year Signed', 'Yrs', 'Total', 'APY', 'Guarantees', 'Amount Earned', 'Percent Earned', 'Effective APY', 'Name']
with open('/Users/namhlahade/Documents/GitHub/NFL-Second-Contract/extensions.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
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
            qbLink = qbURL + a['href'] + '#contract-history'
            newPage = requests.get(qbLink)
            newSoup = BeautifulSoup(newPage.content, "html.parser")
            name = newSoup.find('h3')

            name = name.text.strip()
            div = newSoup.find('div', {'class': 'contract-history'})
            table = div.find('table', {'class':'sortable'})
            tbody = table.find('tbody')
            rows = tbody.find_all('tr')

            for row in rows:
                cols = row.find_all('td')
                cols = [x.text.strip() for x in cols]
                cols.append(name)
                print(cols)
                print(name)
                writer.writerow(cols)
            