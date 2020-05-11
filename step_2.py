import json
import math
import requests
from bs4 import BeautifulSoup

# foreach appid
# extract aim tags multiply weights, sum the points 

url = "https://steamcommunity.com/profiles/76561198355487530"
cookies = {'birthtime': '283993201', 'mature_content': '1'}
sumList = {}
tagLimit = 5
test_time = 0

# count
with open(r"json.txt", 'r', encoding='utf-8') as file:
	for item in file:
		if test_time == 200:
			break
		appid, hour = item.split(" ")
		hour = float(hour)
		gameUrl = "https://store.steampowered.com/app/" + str(appid) + "/"
		gamePage = requests.get(gameUrl, cookies=cookies).content
		soup = BeautifulSoup(gamePage, 'html.parser')
		tags = soup.find_all("a", class_="app_tag")
		count = 0
		for tag in tags:
			tag = tag.get_text().strip()
			if tag in sumList:
				sumList[tag] += round(math.log10(hour) * (4 - count) / 10, 2)
			else:
				sumList[tag] = round(math.log10(hour) * (4 - count) / 10, 2)
			count += 1
			if count == tagLimit:
				break
		test_time += 1
		print("current index: " + str(test_time) + "/200 | current progress: " + str(round(test_time / 2, 2)) + " %")
file.close()
print(sumList)

fw = open("result.txt", 'w')
fw.write(json.dumps(sumList, indent=4))
fw.close()
