
import json
import pandas as pd
import numpy as np


dic_Teams = {1:"Athletic", 2:"Atlético", 3:"Barcelona", 5:"Celta",7:"Espanyol", 8:"Getafe",10:"Levante", 13:"Real Sociedad",
             15:"Real Madrid", 17: "Sevilla", 18: "Valencia", 19: "Villarreal", 70: "Rayo Vallecano", 76: "Eibar", 87: "Betis", 91: "Alavés",
             92:"Leganés", 289: "Girona", 418: "Valladolid", 419: "Huesca"}

class Player:
    def __init__(self, id, name, team,position,price, status, priceIncrement,points,F0, F1, F2, F3,F4, pointsLastSeason):
        self.name = name
        self.id = id
        self.team = team
        self.price = price
        self.position = position
        self.status = status
        self.priceIncrement = priceIncrement
        self.points = points
        self.F0 = F0
        self.F1 = F1
        self.F2 = F2
        self.F3 = F3
        self.F4 = F4
        self.pointsLastSeason = pointsLastSeason

    def to_dict(self):
        return {
            'Name': self.name,
            'ID': self.id,
            'TeamID': self.team,
            'Price': self.price,
            'Position': self.position,
            'Status': self.status,
            'Price Increment': self.priceIncrement,
            'Points': self.points,
            'F0': self.F0,
            'F1': self.F1,
            'F2': self.F2,
            'F3': self.F3,
            'F4': self.F4,
            'Points Last Season': self.pointsLastSeason,
        }


def Create_Player(data):
    fitness = data['fitness']
    return (Player(data['id'],data['name'],data['teamID'],data['position'],
                  data['price'],data['status'],data['priceIncrement'],fitness[0],
                  fitness[1], fitness[2], fitness[3], fitness[4],
                  data['points'], data['pointsLastSeason']))

with open('data.json', encoding='UTF-8') as f:
    data = json.load(f)


df = pd.DataFrame()

players = data['data']['players']

array_players = []

for p, key in enumerate(players):
    array_players.append(Create_Player(players[key]))




df = pd.DataFrame.from_records([s.to_dict() for s in array_players])

df = df.dropna(subset=['TeamID'])
df['TeamID'] = df['TeamID'].astype(int)

df['Team'] = df['TeamID'].apply(lambda x: dic_Teams[x])
df.set_index('Name', inplace=True)



with pd.option_context('display.max_rows', None, 'display.max_columns', 12):
    print(df.sort_values('Price Increment', ascending=False).iloc[0:5])


print(df)