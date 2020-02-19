import requests 
import json
import asyncio
import urllib
import csv
import math
import time
from datetime import datetime
import PySimpleGUI as sg
import pandas as pd 

from ui.main_UI_page import load_main_UI
from utilities.variables import poe_pubStashUrl
from utilities.helpers import test_me, map_offers_details, load_config
import utilities

# Load configuration from config/config.yaml
cfg = load_config()

# ---------------- !!!!!!!!!!!!!! ---------------- #
# ----------------   TEST  ZONE   ---------------- #
# ---------------- !!!!!!!!!!!!!! ---------------- #


# ---------------- !!!!!!!!!!!!!! ---------------- #
# ----------------   TEST  ZONE   ---------------- #
# ---------------- !!!!!!!!!!!!!! ---------------- #



# Load relevant variables from config
sg.ChangeLookAndFeel(cfg['theme'])

# Import base UI Canvas
load_main_UI()


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