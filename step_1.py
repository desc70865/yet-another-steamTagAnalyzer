import re
import json
import requests

# save json to local

minThreshold = 2.0  # set lower

playerId = "76561198355487530"
print("\nGenerating game list...")
url = "https://steamcommunity.com/profiles/" + playerId

cookies = {'birthtime': '283993201', 'mature_content': '1'}
page = requests.get(url + "/games/?tab=all", cookies=cookies).text
want = json.loads(re.search(r"var rgGames = (.*);", page).group(1))

fw = open("json.txt", 'w')
for item in want:
    appid = item['appid']
    hours = item['hours_forever'].replace(",", "")
    if float(hours) > (minThreshold + 1.0):
        fw.write(str(appid)+' '+str(float(hours) - minThreshold))
        fw.write("\n")
    else:
        break
fw.close()
