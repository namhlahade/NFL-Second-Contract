import pandas as pd
import math

df = pd.read_csv ('/Users/namhlahade/Documents/GitHub/NFL-Second-Contract/quarterbackStats.csv')
df2 = pd.read_csv ('/Users/namhlahade/Documents/GitHub/NFL-Second-Contract/quarterbackStats2.csv')
YDS_list = df['YDS'].tolist()
plist = df['NAME'].tolist()
rush_list = df['RUSH YDS'].tolist()
name2 = df2['Player'].tolist()
TDpercentage = df2['TD%']
Intpercentage = df2['Int%']

player_list = []
for player in plist:
    if player not in player_list:
        player_list.append(player)

Stats_dict = {} #Value = pass yards, rush yards, TD percentage / Int percentage
for player in player_list:
    Stats_dict[player] = []

YDS_dict = {}
for player in player_list:
    YDS_dict[player] = []

i = 0
for p in plist:
    YDS_dict[p].append(YDS_list[i])
    i = i+1

for player in player_list:
    YDS_dict[player] = [x for x in YDS_dict[player] if math.isnan(x) == False]

for player in player_list:
    average = 0
    for yd in YDS_dict[player]:
        average = average + yd
    average = average/len(YDS_dict[player])
    YDS_dict[player] = average

for player in player_list:
    Stats_dict[player].append(YDS_dict[player])

RushYDS_dict = {}
for player in player_list:
    RushYDS_dict[player] = []

j = 0
for p in plist:
    RushYDS_dict[p].append(rush_list[j])
    j = j+1

for player in player_list:
    RushYDS_dict[player] = [x for x in RushYDS_dict[player] if math.isnan(x) == False]

for player in player_list:
    average = 0
    for yd in RushYDS_dict[player]:
        average = average + yd
    average = average/len(RushYDS_dict[player])
    RushYDS_dict[player] = average

for player in player_list:
    Stats_dict[player].append(RushYDS_dict[player])

TDInt_dict = {}
for player in player_list:
    TDInt_dict[player] = []

name3 = []
for name in name2:
    name = name.replace("*", "")
    name = name.replace("+", "")
    name = name.replace("*+", "")
    name3.append(name)

TDdict = dict(zip(name3, TDpercentage));

for name in name3:
    if name in Stats_dict.keys():
        TDInt_dict[name].append(TDdict[name])
    if "III" in name:
        name2 = name.replace(" III", "")
        if name2 in Stats_dict.keys():
            TDInt_dict[name2].append(TDdict[name])
    if "II" in name:
        name2 = name.replace(" II", "")
        if name2 in Stats_dict.keys():
            TDInt_dict[name2].append(TDdict[name])

Intdict = dict(zip(name3, Intpercentage))

for name in name3:
    if name in Stats_dict.keys():
        TDInt_dict[name].append(Intdict[name])
    if "III" in name:
        name2 = name.replace(" III", "")
        if name2 in Stats_dict.keys():
            TDInt_dict[name2].append(TDdict[name])
    if "II" in name:
        name2 = name.replace(" II", "")
        if name2 in Stats_dict.keys():
            TDInt_dict[name2].append(TDdict[name])

for item in TDInt_dict:
    if TDInt_dict[item][1] != 0:
        ratio = TDInt_dict[item][0]/TDInt_dict[item][1]

    else:
        ratio = 10
    TDInt_dict[item] = ratio

for player in player_list:
    Stats_dict[player].append(TDInt_dict[player])

print(Stats_dict)
#He