import requests 
import json
import asyncio
import urllib
import aiohttp
from asyncio_throttle import Throttler
import nest_asyncio

nest_asyncio.apply()

class RateLimitException(Exception):
    pass


def fetch_offers(league, currency_pairs, item_list, limit=20):
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(
        fetch_offers_async(league, currency_pairs, item_list, limit))
    return results


async def fetch_offers_async(league, currency_pairs, item_list, limit=10):
    throttler = Throttler(10)
    
    async with aiohttp.ClientSession() as sess:
        tasks = [
            asyncio.ensure_future(
                fetch_offers_for_pair(sess, throttler, league, p[0], p[1], item_list,
                                      limit)) for p in currency_pairs
        ]
        for p in currency_pairs:
            print(p[0], [p[1]])
        (done, _not_done) = await asyncio.wait(tasks)
        results = [task.result() for task in done]
        return results


"""
Private helpers below
"""


async def fetch_offers_for_pair(sess, throttler, league, want, have, item_list, limit=5):
    async with throttler:
        offer_ids = []
        query_id = None
        offers = []
        
        offer_id_url = "http://www.pathofexile.com/api/trade/exchange/{}".format(
            urllib.parse.quote(league))
        payload = {
            "exchange": {
                "status": {
                    "option": "online"
                },
                "have": have,
                "want": want,
            }
        }

        response = await sess.request("POST", url=offer_id_url, json=payload)
        try:
            json = await response.json()
            offer_ids = json["result"]
            query_id = json["id"]
        except Exception:
            print("Rate limited during initial fetch")
        if len(offer_ids) != 0:

            id_string = ",".join(offer_ids[:limit])
            url = "http://www.pathofexile.com/api/trade/fetch/{}?query={}&exchange".format(
                id_string, query_id)
            
            response = await sess.get(url)
            try:
                json = await response.json()
                offers = [map_offers_details(x) for x in json["result"]]
            except Exception:
                print("Rate limited during second fetch")
            
        return {"trading": have+"->"+want, "offers": offers}

def map_offers_details(offer_details):
    contact_ign = offer_details["listing"]["account"]["lastCharacterName"]
    stock = offer_details["listing"]["price"]["item"]["stock"]
    receive = offer_details["listing"]["price"]["item"]["amount"]
    pay = offer_details["listing"]["price"]["exchange"]["amount"]
    conversion_rate = round(receive / pay, 4)

    return {
        "contact_ign": contact_ign,
        "conversion_rate": conversion_rate,
        "stock": stock,
    }