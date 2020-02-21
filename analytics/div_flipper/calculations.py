import csv
import requests
import abc
import PySimpleGUI as sg
league = 'Metamorph'
from utilities.general_functions import timestamp_string

# noinspection PyBroadException
class APIAgent(abc.ABC):
    """
    Abstract agent for accessing APIs

    Attributes:
        APIAgent._mean_name: the name with which the api describes the average price (in chaos orbs) of an item
        APIAgent._api_url: the url through which to access the API
        APIAgent._id_file: the filename with names of div cards and item ids of their rewards
        APIAgent._id_dict: a dictionary containing the contents of id_file
        APIAgent._supported_cards: a list of cards which are supported
    """

    _mean_name = ''
    _api_url = ''
    _id_file = ''
    _id_dict: dict = {}
    _supported_cards = []

    def __init__(self, league: str):
        """Initializes an agent for league LEAGUE. The API is determined by the instantiating subclass."""
        # TODO: add selection option from active leagues (standard sc/hc and challenge sc/hc)
        self._league = league
        self._data = self._fetch_div_data()
        self._filter_name()
        self._item_data = self._fetch_all_data()
        self._trim_data()

    @staticmethod
    def _load_id_dict(file_name):
        """Loads and returns a dictionary of the supported div cards and the item ids of their rewards"""
        # TODO: implement functionality to support rewards containing stacks of items
        with open(file_name, 'r', newline='') as f:
            reader = csv.reader(f, delimiter=',')
            id_dic = {row[0]: int(row[1]) for row in reader}
        return id_dic

    def save_data(self):
        """Saves self.data as a csv file."""
        filename = 'data/div_flipper/' + 'div-flipping-' + timestamp_string() + '.csv'
        with open(filename, 'w', newline='') as f:
            wtr = csv.writer(f)
            wtr.writerow(self._data[0].keys())
            for dic in self._data:
                wtr.writerow(dic.values())

    # API methods

    @classmethod
    @abc.abstractmethod
    def _api(cls, func, params):
        """Accesses the API (dependent on the instantiating subclass) with function FUNC and parameters
        PARAMS, returning the JSON value."""
        
        print('calling', func, params, 'to', cls._api_url)
        result = requests.get(cls._api_url + func, params=params)
        try:
            return result.json()
        except:
            print(result.status_code)

    @abc.abstractmethod
    def _fetch_div_data(self):
        """Fetches data of all div cards from API (of instantiating subclass)."""
        pass

    @abc.abstractmethod
    def _fetch_all_data(self):
        """Fetches data on all items from API (of instantiating subclass)."""
        pass

    # Operations on APIAgent.data

    def _trim_data(self):
        """Selects the name, stackSize, and current price entries of each entry of self.data"""

        def select(dic):
            return {entry: dic[entry] for entry in ['name', 'stackSize', self._mean_name]}

        self._data = list(map(select, self._data))

    def _filter_name(self):
        """Filters div cards to only ones that are supported"""
        self._data = list(filter(lambda dic: dic['name'] in self._supported_cards, self._data))

    def filter_price(self, floor=40, ceil=2000):
        """Filters div cards with totalCost between FLOOR and CEIL"""
        self._data = list(filter(lambda dic: floor <= dic[self._mean_name] * dic['stackSize'] <= ceil, self._data))

    def calculate_profit(self):
        """Performs various calculations on self.data and sorts the results based on profit/trade and yield."""
        for div in self._data:
            div['totalCost'] = div[self._mean_name] * div['stackSize']
            div['rewardID'] = self._id_dict[div['name']]
            div['totalRevenue'] = self._lookup_price(div['rewardID'], div['name'])
            div['profit'] = (div['totalRevenue'] - div['totalCost'])
            div['profitPerTrade'] = div['profit'] / (div['stackSize'] + 1)
            div['% ROI'] = (div['totalRevenue'] - div['totalCost']) / div['totalCost']
            div['profitMargin'] = div['profit'] / (1+ div['totalRevenue'])
        self._data.sort(key=lambda d: d['% ROI'], reverse=True)

    def _lookup_price(self, target_id, name):
        """Uses binary search to look up and return the current price of item with id TARGET_ID."""

        def lookup_recursive(lower, upper):
            i = (lower + upper) // 2  # the midpoint of the two bounds
            current_id = self._item_data[i]['id']  # id of the midpoint

            if current_id == target_id:
                return self._item_data[i][self._mean_name]
            elif lower == upper:
                print('name', name, 'with id', target_id, 'not found in', self._league)
                return 0
            elif current_id < target_id:
                if upper - lower == 1:
                    i += 1
                return lookup_recursive(i, upper)
            elif current_id > target_id:
                return lookup_recursive(lower, i)

        return lookup_recursive(0, len(self._item_data) - 1)


class WatchAPIAgent(APIAgent):
    _mean_name = 'mean'
    _api_url = 'http://api.poe.watch/'
    _id_file = 'analytics/div_flipper/watch_item_ids.csv'
    _id_dict: dict = APIAgent._load_id_dict(_id_file)
    _supported_cards = _id_dict.keys()

    @classmethod
    def _api(cls, func, params):
        return super()._api(func, params)

    def _fetch_all_data(self):
        return self._api('compact', {'league': self._league})

    def _fetch_div_data(self):
        return self._api('get', {'league': self._league, 'category': 'card'})


class NinjaAPIAgent(APIAgent):
    _mean_name = 'chaosValue'
    _api_url = 'https://poe.ninja/api/Data/'
    _id_file = 'analytics/div_flipper/ninja_item_ids.csv'
    _id_dict: dict = APIAgent._load_id_dict(_id_file)
    _supported_cards = _id_dict.keys()

    @classmethod
    def _api(cls, func, params):
        return super()._api(func, params)['lines']

    def _fetch_all_data(self):
        with open('analytics/div_flipper/ninja_itemoverview_types.csv', 'r', newline='') as f:
            reader = csv.reader(f, delimiter=',')
            types = [item for sublist in reader for item in sublist]
        all_data = []
        i = 1
        for func in types:
            print(func)
            sg.OneLineProgressMeter('Div Card Analysis', i, len(types),  'key', 'Running various divination card lookups and calculations.')
            i = i+1
            all_data.extend(self._api('itemoverview', {'league': self._league, 'type': func}))
        # TODO: Implement support for currencies and fragments (different format) here
        all_data.sort(key=lambda dic: dic['id'])
        return all_data

    def _fetch_div_data(self):
        return self._api('itemoverview?league=Metamorph&type=DivinationCard', {'league': self._league})

def run_flipper():
    #agent = APIAgent.WatchAPIAgent(league)
    agent = NinjaAPIAgent(league)
    # agent.filter_price()

    agent.calculate_profit()
    agent.save_data()
    sg.OneLineProgressMeterCancel('key')