import json 

div_cards = []
with open('div_card_data.json') as f:
    data = json.load(f)
    with open('div_card_pairs.txt', 'w') as g:
        for p in data['lines']:
            g.write(str(p['id']) + "," + str(p['name'])+"\n")
    with open('div_card_itemNames.txt', 'w') as h:
        for p in data['lines']:
            h.write(str(p['explicitModifiers'][0]))