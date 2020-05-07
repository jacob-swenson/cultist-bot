from lor_deckcodes import LoRDeck, CardCodeAndCount
import json
import os

LOR_DATA_FOLDER = 'cultist-bot/data/lor/'


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


def get_card_data_by_code(card):
    for card_data in set_data:
        if card_data["cardCode"] == card:
            return card_data
    return None


set_data = []
for filename in os.listdir(LOR_DATA_FOLDER):
    if filename.endswith(".json"):
        with open(LOR_DATA_FOLDER + filename) as f:
            cur_set = json.load(f)
            for val in cur_set:
                set_data.append(val)
