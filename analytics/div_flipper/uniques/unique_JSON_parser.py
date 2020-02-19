import json 


def extract_values(obj, key):
    """Pull all values of specified key from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results
	
with open('unique_accessory_data.json') as f:
    data = json.load(f)
    itemNames = extract_values(data, 'name')
    itemIDs = extract_values(data, 'id') 
    
    joinTogether = dict(zip(itemNames, itemIDs))
    
    with open('unique_accessory_itemList.txt', 'w') as g:
        for key in joinTogether.keys():
            g.write("%s,%s\n"%(key, joinTogether[key]))