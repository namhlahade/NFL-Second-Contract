from bs4 import BeautifulSoup
import requests
import csv

names = ["Aaron Rodgers", "Tom Brady", "Patrick Mahomes", "Deshaun Watson", "Russell Wilson", "Lamar Jackson", "Ryan Tannehill", "Justin Herbert", "Kyler Murray", "Baker Mayfield", "Derek Carr","Matthew Stafford", "Matt Ryan", "Kirk Cousins", "Dak Prescott", "Philip Rivers", "Joe Burrow", "Drew Brees", "Ben Roethlisberger", "Ryan Fitzpatrick", "Jared Goff", "Jalen Hurts", "Daniel Jones", "Andy Dalton", "Taysom Hill", "Alex Smith", "Tua Tagovailoa", "Teddy Bridgewater", "Jimmy Garoppolo", "Mitchell Trubisky", "Cam Newton", "Drew Lock", "Gardner Minshew", "Carson Wentz", "Sam Darnold", "Taylor Heinicke"]
header = ["Contract Terms", "Signing Bonus", "Average Salary", "GTD at Sign", "Total GTD", "Free Agent"] 
 
URL = "https://www.nfl.com/players/"

header = ['WK','Game Date','OPP', 'RESULT', 'COMP', 'ATT', 'YDS', 'AVG', 'TD', 'INT', 'SCK', 'SCKY', 'RATE', 'RUSH ATT', 'RUSH YDS', 'RUSH AVG', 'RUSH TD', 'FUM', 'LOST', 'NAME']
with open('/Users/namhlahade/Desktop/Football_Project/quarterbackStats.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)

    for quarterback in names:
        quarterbackRaw = quarterback
        quarterback = quarterback.replace(" ", "-")
        quarterbackURL = URL + quarterback + "/stats/logs/2020/"
        page = requests.get(quarterbackURL)
        soup = BeautifulSoup(page.content, "html.parser")
        

        table_body = soup.find('tbody')
        rows = table_body.find_all('tr')

        for row in rows:
            cols = row.find_all('td')
            cols = [x.text.strip() for x in cols]
            cols.append(quarterbackRaw)
            print (cols)
            writer.writerow(cols)
    
