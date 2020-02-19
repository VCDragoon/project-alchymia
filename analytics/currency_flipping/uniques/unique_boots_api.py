import json 
import requests

r = requests.get("https://poe.ninja/api/data/itemoverview?league=Metamorph&type=UniqueArmour")

print(r.status_code) 
print(json.dumps(r.text))

with open('unique_armour.txt', 'w') as f:
    json.dump(r.text, f)

    