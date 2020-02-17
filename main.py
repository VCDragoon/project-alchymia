import requests 
import json
import asyncio
import urllib
import csv
import math
import time
from datetime import datetime


import utilities

pubStashUrl = "http://www.pathofexile.com/api/public-stash-tabs?id="

r = requests.get(pubStashUrl)
stashes = r.json()
nextPageId = stashes["next_change_id"]
stashIds = [nextPageId + ".0"]
stashDict = {nextPageId: stashes["stashes"]}