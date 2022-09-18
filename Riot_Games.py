from typing import Type
import requests
import plotly.express as pe
import pandas

apikey = "YOUR API KEY GOES HERE"
url1 = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
username = input("Enter summoner name (It's case sensitive!): ")

geturl = url1 + username + "?" + apikey

rawdata = requests.get(geturl)

puuid = rawdata.json()['puuid']

url2 = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/" + puuid +"/ids?type=ranked&start=0&count=20" + "&" + apikey

matchIDs = requests.get(url2).json()
user_list_roles = []
url3 = "https://americas.api.riotgames.com/lol/match/v5/matches/" + "i" + "?" + apikey
data = requests.get(url3).json()

topCount = 0
jngCount = 0
midCount = 0
adcCount = 0
supCount = 0


for i in matchIDs:
    url3 = "https://americas.api.riotgames.com/lol/match/v5/matches/" + i + "?" + apikey
    data = requests.get(url3).json()
    for j in data['info']['participants']:
        if j['summonerName'] == username:
            user_list_roles.append(j['individualPosition'])

for i in user_list_roles:
    if i == "TOP":
        topCount += 1
    if i == "JUNGLE":
        jngCount += 1
    if i == "MIDDLE":
        midCount += 1
    if i == "BOTTOM":
        adcCount += 1
    if i == "UTILITY":
        supCount += 1

names = [["Top",topCount], ["Jungle", jngCount], ["Middle", midCount], ["ADC", adcCount],["Support", supCount]]



fig = pe.pie(pandas.DataFrame(names, columns=['Role','Amount Played']), values= "Amount Played", names = "Role")
fig.show()

print(user_list_roles)
print("\nTop Count: %d\nJungle Count: %d\nMid Count: %d\nADC Count: %d\nSupport Count: %d" %(topCount, jngCount, midCount, adcCount, supCount))
