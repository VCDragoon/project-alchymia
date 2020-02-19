import json 
import requests

r = requests.get("https://poe.ninja/api/data/itemoverview?league=Metamorph&type=DivinationCard")

print(r.status_code) 
print(json.dumps(r.text))

with open('div_data.txt', 'w') as f:
    json.dump(r.text, f)

    