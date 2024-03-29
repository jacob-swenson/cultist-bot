from lor_deckcodes import LoRDeck, CardCodeAndCount
from fuzzywuzzy import process
from dotenv import load_dotenv
import requests
import json
import os
import zipfile
import time
import shutil

load_dotenv()
LOR_DATA_FOLDER = 'data/lor/'
LOR_BASE_URL = 'https://dd.b.pvp.net'
LOR_LOCALIZATION = 'en_us'
LOR_VERSION = os.getenv('LOR_VERSION', '1_0_0')
LOR_SETS = int(os.getenv('LOR_SETS', 2))
REPEAT = os.getenv('REPEAT', 30)
ALWAYS_DOWNLOAD = os.getenv('ALWAYS_DOWNLOAD') == "True"

print('LOR_VERSION=' + LOR_VERSION)
print('LOR_SETS=' + str(LOR_SETS))

card_names = []
set_data = []
emote_data = []
emote_names = []
possible_entries = []


class Deck:
    def __init__(self, code):
        deck = LoRDeck.from_deckcode(code)
        cards = []
        self.champions = []
        self.regions = []
        self.cards_by_region = {}
        self.cards_by_type = {"Champions": [], "Followers": [], "Spells": [], "Landmarks": []}
        for cardcode in deck:
            card = CardCodeAndCount.from_card_string(cardcode)
            for card_data in set_data:
                if card_data["cardCode"] == cardcode[2:]:
                    card_region = ""
                    if card_data["rarity"] == "Champion":
                        self.champions.append(card_data["name"])
                        self.cards_by_type["Champions"].append(Card(card.count, card_data))
                    elif card_data["type"] == "Unit":
                        self.cards_by_type["Followers"].append(Card(card.count, card_data))
                    elif card_data["type"] == "Spell":
                        self.cards_by_type["Spells"].append(Card(card.count, card_data))
                    else:
                        self.cards_by_type["Landmarks"].append(Card(card.count, card_data))
                    for region in card_data["regions"]:
                        card_region += region + " "
                        if region not in self.regions:
                            self.regions.append(region)
                            self.cards_by_region[region] = []
                    cards.append(Card(card.count, card_data))
                    self.cards_by_region[card_data["regions"][0]].append(Card(card.count, card_data))
        self.cards = sorted(cards, key=lambda x: x.data["cost"])
        for k, v in self.cards_by_region.items():
            self.cards_by_region[k] = sorted(v, key=lambda x: x.data["cost"])
        for k, v in self.cards_by_type.items():
            self.cards_by_type[k] = sorted(v, key=lambda x: x.data["cost"])


class Card:
    def __init__(self, count: int, data: json):
        self.count = count
        self.data = data


def get_card_data_by_name(card):
    for card_data in set_data:
        if card_data["name"].lower() == card.lower():
            return card_data
    return None


def get_emote_by_name(emote):
    for element in emote_data:
        if element["name"].lower() == emote.lower() or element["keyword"].lower() == emote.lower():
            return element
    return None


def get_card_data_by_fuzzy_search(card):
    if len(card_names) == 0:
        for card_data in set_data:
            card_names.append(card_data["name"])
    best_guess = process.extractOne(card, card_names)
    print(f"Fuzzy Wuzzy is {best_guess[1]}% sure the user is looking for {best_guess[0]}")
    return get_card_data_by_name(best_guess[0])


def get_emote_by_fuzzy_search(emote):
    if len(emote_names) == 0:
        for element in emote_data:
            emote_names.append(element["name"])
    if len(possible_entries) == 0:
        for name in emote_names:
            possible_entries.append(name)
            possible_entries.append(get_emote_by_name(name)["keyword"])
    if len(emote) == 0:
        return None
    best_guess = process.extractOne(emote, possible_entries)
    print(f"Fuzzy Wuzzy is {best_guess[1]}% sure the user is looking for {best_guess[0]}")
    return get_emote_by_name(best_guess[0])


def get_emote_names():
    if len(emote_names) == 0:
        for element in emote_data:
            emote_names.append([element["name"]])
    result = 'Emotes I know:\n'
    for name in emote_names:
        result += f'{name} - {get_emote_by_name(name)["keyword"]}\n'
    return result


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
                req = requests.get(url)
                with open(zip_filename,'wb') as output_file:
                    output_file.write(req.content)
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
    if ALWAYS_DOWNLOAD:
        shutil.rmtree(LOR_DATA_FOLDER + LOR_VERSION)
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

with open(LOR_DATA_FOLDER + 'emotes/emotes.json') as f:
    emote_data = json.load(f)
