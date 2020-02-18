import requests 
import json
import asyncio
import urllib
import csv
import math
import time
from datetime import datetime
import PySimpleGUI as sg

from utilities.variables import poe_pubStashUrl
from utilities.helpers import test_me, map_offers_details, load_config
import utilities

# Load configuration from config/config.yaml
cfg = load_config()

# Import configured variables
poe_pubStashUrl = cfg['URLs']['poe_pubStashUrl']

sg.ChangeLookAndFeel('DarkBlue4')

# Edit/View Configuration
layout = []
for k, v in cfg["URLs"].items():
    layout += [sg.Text(f'{k}'), sg.In(f'{v}', key=v)],
layout += [[sg.Button('Save'), sg.Button('Exit')]]

window = sg.Window('Alchymia Configuration', layout)
event, values = window.read()


# r = requests.get(poe_pubStashUrl)
# stashes = r.json()
# nextPageId = stashes["next_change_id"]
# stashIds = [nextPageId + ".0"]
# stashDict = {nextPageId: stashes["stashes"]}

# for page in range(1, 10):
    
#     r = requests.get(poe_pubStashUrl + nextPageId)
#     stashes = r.json()    
    
#     nextPageId = stashes["next_change_id"]
#     stashIds.append(nextPageId + "." + str(page))
#     stashDict[nextPageId] = stashes["stashes"]