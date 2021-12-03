from bs4 import BeautifulSoup
import requests
import csv

names = ["Aaron Rodgers", "Tom Brady", "Patrick Mahomes", "Deshaun Watson", "Russell Wilson", "Lamar Jackson", "Ryan Tannehill", "Justin Herbert", "Kyler Murray", "Baker Mayfield", "Derek Carr","Matthew Stafford", "Matt Ryan", "Kirk Cousins", "Dak Prescott", "Philip Rivers", "Joe Burrow", "Drew Brees", "Ben Roethlisberger", "Ryan Fitzpatrick", "Jared Goff", "Jalen Hurts", "Daniel Jones", "Andy Dalton", "Taysom Hill", "Alex Smith", "Tua Tagovailoa", "Teddy Bridgewater", "Jimmy Garoppolo", "Mitchell Trubisky", "Cam Newton", "Drew Lock", "Gardner Minshew", "Carson Wentz", "Sam Darnold", "Taylor Heinicke", "Mac Jones"]

teams = ['arizona cardinals', 'atlanta falcons', 'baltimore ravens', 'buffalo bills', 'carolina panthers', 'chicago bears', 'cincinatti bengals', 'cleveland browns', 'dallas cowboys', 'denver broncos', 'detroit lions', 'greenbay packers', 'houstan texans', 'indianapolis colts', 'jacksonville jaguars', 'kansas city chiefs', 'las vegas raiders', 'los angeles rams', 'miami dolphins', 'minnesota vikings', 'new england patriots', 'new york giants', 'new york gets', 'philadelphia eagles', 'pittsburgh steelers', 'san francisco 49ers', 'seattle seahawks', 'tampa bay buccaneers', 'tennessee titans', 'washington football team']
header = ["Contract Terms", "Signing Bonus", "Average Salary", "GTD at Sign", "Total GTD", "Free Agent"] 

URL = "https://www.spotrac.com/nfl/"

with open('/Users/namhlahade/Desktop/Football_Project/quarterbackContracts.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    for team in teams:
        teamName = team
        team = team.replace(" ", "-")
        teamURL = URL + team + "/cap/"
        page = requests.get(teamURL)
        soup = BeautifulSoup(page.content, "html.parser")
        for link in soup.find_all('a'):
            for name in names:
                if (name == link.string):
                    newURL = link.get('href')
                    newpage = requests.get(newURL)
                    soup2 = BeautifulSoup(newpage.content, "html.parser")
                    
                    table_body = soup2.find('tbody')
                    rows = table_body.find_all('tr')

                    for row in rows:
                        cols = row.find_all('td')
                        cols = [x.text.strip() for x in cols]
                        print (name)
                        writer.writerow(cols)