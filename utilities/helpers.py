#TODO change over to class structure instead
#TODO add not just for map, but for all kinds of stuff (currency, cards, etc.)
import yaml
import pandas as pd

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

def test_me():
    print("I'm Tested!")

# Loads configuration YAML file from local reference to config.yaml
def load_config():
    with open("config/config.yaml", 'r') as ymlfile:
        try:
            cfg = yaml.safe_load(ymlfile)
            return cfg
        except yaml.YAMLError as exc:
            print(exc)


def highlight_diff(data, color='yellow'):
    attr = 'background-color: {}'.format(color)
    other = data.xs('First', axis='columns', level=-1)
    return pd.DataFrame(np.where(data.ne(other, level=0), attr, ''),
                        index=data.index, columns=data.columns)