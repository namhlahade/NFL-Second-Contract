from bs4 import BeautifulSoup
import requests
import csv

header = ["NAME", "QBR","PAA","PLAYS", "EPA","PASS","RUN","SACK","PEN","RAW"]
names = ["Patrick Mahomes", "Josh Allen", "Aaron Rodgers", "Russell Wilson", "Justin Herbert", "Kyler Murray", "Deshaun Watson", "Ryan Tannehill", "Tom Brady", "Derek Carr", "Matt Ryan", "Baker Mayfield", "Lamar Jackson", "Matthew Stafford", "Kirk Cousins", "Ben Roethlisberger", "Philip Rivers", "Teddy Bridgewater", "Drew Brees", "Jared Goff", "Daniel Jones", "Ryan Fitzpatrick", "Joe Burrow", "Drew Lock", "Cam Newton", "Mitchell Trubisky", "Carson Wentz", "Tua Tagovailoa", "Gardner Minshew", "Andy Dalton", "Sam Darnold", "Nick Foles", "Nick Mullens"]
dak = ["Dak Prescott", "71.9", "48.1", "690", "93.1", "70.7", "10", "-9.7", "2.6", "72.8"]
URL = "https://www.espn.com/nfl/qbr/_/season/2020/seasontype/2/sort/cwepaTotal/dir/desc"
with open('/Users/namhlahade/Documents/GitHub/NFL-Second-Contract/quarterbackstats3.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    table = soup.find_all('tbody')
    secondTable = table[1]
    rows = secondTable.find_all('tr')

    i = 0
    for row in rows:
        cols = row.find_all('td')
        cols = [x.text.strip() for x in cols]
        cols.insert(0, names[i])
        writer.writerow(cols)
        i = i+1
    writer.writerow(dak)
    


