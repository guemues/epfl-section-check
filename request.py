import requests
import pprint
import json

url = "http://www.betexplorer.com/gres/ajax/matchodds.php"

querystring = {"e":"tfNcjRTa","b":"ou"}

headers = {
    'referer': "XXX/XXX/XXX/XXX/XXX/XXX/"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

with open("hello.txt", "w") as f: 
    json.dump(response.json(), f)