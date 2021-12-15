from bs4 import BeautifulSoup
import requests
import csv

header = ['Year', 'No.', 'Round', 'Pick', 'Player', 'Name', 'Team', 'College']

with open('/Users/namhlahade/Documents/GitHub/NFL-Second-Contract/rookieQBs.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)

    URL = "http://www.drafthistory.com/index.php/positions/qb"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    body = soup.find('body')
    div = body.find('div', {'id': 'main'})
    table = div.find('table', {'border': '1'})
    rows = table.find_all('tr')
    year = 0
    for row in rows:
        cols = row.find_all('td')
        cols = [x.text.strip() for x in cols]
        if cols:
            if 'Quarterbacks' not in cols:
                if cols[0] == '':
                    cols[0] = year
                if 's' in cols[0]:
                    cols[0] = cols[0].replace('s', '')
                if 'u' in cols[0]:
                    cols[0] = cols[0].replace('u', '')
                if cols[0] != '':
                    year = cols[0]
                if int(cols[0]) >= 1970:
                    writer.writerow(cols)