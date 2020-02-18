import requests 
import json
import asyncio
import urllib
import csv
import math
import time
from datetime import datetime
from utilities.variables import poe_pubStashUrl
from utilities.helpers import test_me, map_offers_details
import utilities

r = requests.get(poe_pubStashUrl)
stashes = r.json()
nextPageId = stashes["next_change_id"]
stashIds = [nextPageId + ".0"]
stashDict = {nextPageId: stashes["stashes"]}

for page in range(1, 10):
    
    r = requests.get(poe_pubStashUrl + nextPageId)
    stashes = r.json()    
    
    nextPageId = stashes["next_change_id"]
    stashIds.append(nextPageId + "." + str(page))
    stashDict[nextPageId] = stashes["stashes"]