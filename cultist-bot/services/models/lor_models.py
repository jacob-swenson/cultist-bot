from lor_deckcodes import LoRDeck, CardCodeAndCount
from fuzzywuzzy import process
from urllib import request
import json
import os
import zipfile
import time

LOR_DATA_FOLDER = 'data/lor/'
LOR_BASE_URL = 'https://dd.b.pvp.net'
LOR_LOCALIZATION = 'en_us'
LOR_VERSION = '2_0_0'
LOR_SETS = 3
REPEAT = 1000

card_names = []
set_data = []


class Deck:
    def __init__(self, code):
        deck = LoRDeck.from_deckcode(code)
        cards = []
        self.champions = []
        self.regions = []
        self.cards_by_region = {}
        for cardcode in deck:
            card = CardCodeAndCount.from_card_string(cardcode)
            for card_data in set_data:
                if card_data["cardCode"] == cardcode[2:]:
                    if card_data["rarity"] == "Champion":
                        self.champions.append(card_data["name"])
                    if card_data["region"] not in self.regions:
                        self.regions.append(card_data["region"])
                        self.cards_by_region[card_data["region"]] = []
                    cards.append(Card(card.count, card_data))
                    self.cards_by_region[card_data["region"]].append(Card(card.count, card_data))
        self.cards = sorted(cards, key=lambda x: x.data["cost"])
        for k, v in self.cards_by_region.items():
            self.cards_by_region[k] = sorted(v, key=lambda x: x.data["cost"])


class Card:
    def __init__(self, count: int, data: json):
        self.count = count
        self.data = data


def get_card_data_by_name(card):
    for card_data in set_data:
        if card_data["name"].lower() == card.lower():
            return card_data
    return None


def get_card_data_by_fuzzy_search(card):
    if len(card_names) == 0:
        for card_data in set_data:
            card_names.append(card_data["name"])
    best_guess = process.extractOne(card, card_names)
    print(f"Fuzzy Wuzzy is {best_guess[1]}% sure the user is looking for {best_guess[0]}")
    return get_card_data_by_name(best_guess[0])


def get_card_data_by_code(card):
    for card_data in set_data:
        if card_data["cardCode"] == card:
            return card_data
    return None


def download_sets(version, sets):
    path = LOR_DATA_FOLDER + version + '/'
    if not os.path.exists(path):
        os.mkdir(path)
    elif not os.path.isdir(path):
        os.remove(path)
        os.mkdir(path)
    for num in range(1, sets + 1):
        set_number = 'set' + str(num) + '-lite-' + LOR_LOCALIZATION
        url = LOR_BASE_URL + '/' + version + '/' + set_number + '.zip'
        print('Downloading: ' + url)
        zip_filename = path + set_number + '.zip'
        repeat = True
        while repeat:
            try:
                request.urlretrieve(url, zip_filename)
                repeat = False
            except Exception as e:
                print("Download failed!")
                if REPEAT > 0:
                    print("Retrying in " + str(REPEAT) + " seconds.")
                    time.sleep(REPEAT)
                    repeat = True
                else:
                    print("Not Retrying")
                    exit(1)
        print('Unzipping: ' + zip_filename)
        with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
            zip_ref.extractall(path)


def sets_downloaded(version, sets):
    if not os.path.exists(LOR_DATA_FOLDER + LOR_VERSION):
        return False
    if not os.path.isdir(LOR_DATA_FOLDER + LOR_VERSION):
        return False
    for num in range(1, sets + 1):
        if not os.path.isfile(LOR_DATA_FOLDER + version + '/' + LOR_LOCALIZATION + '/data/set' + str(num) + '-' +
                              LOR_LOCALIZATION + '.json'):
            return False
    return True


if not sets_downloaded(LOR_VERSION, LOR_SETS):
    print("Downloading new set data")
    download_sets(LOR_VERSION, LOR_SETS)

localized_data = LOR_DATA_FOLDER + LOR_VERSION + '/' + LOR_LOCALIZATION + '/data/'
for num in range(1, LOR_SETS + 1):
    set_filename = 'set' + str(num) + '-' + LOR_LOCALIZATION + '.json'
    with open(localized_data + set_filename) as f:
        cur_set = json.load(f)
        for val in cur_set:
            set_data.append(val)
