from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

qbData = pd.read_csv('/Users/namhlahade/Documents/GitHub/NFL-Second-Contract/rookieQBs.csv')
names = qbData['Name'].tolist()
years = qbData['Year'].tolist()

zip_iterator = zip(names, years)
qbDictionary = dict(zip_iterator)
URL = 'https://www.pro-football-reference.com/players/'
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

ALLPlayers = {}
for letter in alphabet:
    newURL = URL + letter
    page = requests.get(newURL)
    soup = BeautifulSoup(page.content, "html.parser")
    for link in soup.find_all('a'):
        if '/players/'+letter in link.get('href') :
            ALLPlayers[link.string] = link.get('href')

URL2 = 'https://www.pro-football-reference.com'
QuarterBackLinks = {}
for name in names:
    if name in ALLPlayers.keys():
        QuarterBackLinks[name] = URL2 + ALLPlayers[name]

header = ['Name', 'Link']
with open('/Users/namhlahade/Documents/GitHub/NFL-Second-Contract/relevantLinks.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for quarterback in QuarterBackLinks.keys():
        col = [quarterback, QuarterBackLinks[quarterback]]
        writer.writerow(col)
