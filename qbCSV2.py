from bs4 import BeautifulSoup
import requests
import csv

URL = 'https://www.pro-football-reference.com/years/2020/passing.htm'
header = ['Player', 'Tm', 'Age', 'Pos', 'G', 'GS', 'QBrec', 'Cmp', 'Att', 'Cmp', 'Yds', 'TD', 'TD%', 'Int', 'Int%', '1D', 'Lng', 'Y/A', 'AY/A', 'Y/C', 'Y/G', 'Rate', 'QBR', 'Sk', 'Yds', 'Sk%', 'NY/A', 'ANY/A', '4QC', 'GWD']
with open('/Users/namhlahade/Desktop/Football_Project/quarterbackStats2.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    table_body = soup.find('tbody')
    rows = table_body.find_all('tr')

    table_body = soup.find('tbody')
    rows = table_body.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        cols = [x.text.strip() for x in cols]
        print (cols)
        writer.writerow(cols)