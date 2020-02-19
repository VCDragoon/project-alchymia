import json 
import requests

r = requests.get("https://poe.ninja/api/data/itemoverview?league=Metamorph&type=Currency")

print(r.status_code) 
print(json.dumps(r.text))

with open('currency.txt', 'w') as f:
    json.dump(r.text, f)

    