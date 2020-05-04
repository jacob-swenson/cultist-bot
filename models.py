from lor_deckcodes import LoRDeck, CardCodeAndCount
import json


class Deck:
    def __init__(self, code):
        deck = LoRDeck.from_deckcode(code)
        cards = []
        self.champions = []
        self.regions = []
        self.cards_by_region = {}
        for cardcode in deck:
            card = CardCodeAndCount.from_card_string(cardcode)
            if card.set == 1:
                cardset = set1
            elif card.set == 2:
                cardset = set2
            for set_card in cardset:
                if set_card["cardCode"] == cardcode[2:]:
                    if set_card["rarity"] == "Champion":
                        self.champions.append(set_card["name"])
                    if set_card["region"] not in self.regions:
                        self.regions.append(set_card["region"])
                        self.cards_by_region[set_card["region"]] = []
                    cards.append(Card(card.count, set_card))
                    self.cards_by_region[set_card["region"]].append(Card(card.count, set_card))
        self.cards = sorted(cards, key=lambda x: x.data["cost"])
        for k, v in self.cards_by_region.items():
            self.cards_by_region[k] = sorted(v, key=lambda x: x.data["cost"])


class Card:
    def __init__(self, count: int, data: json):
        self.count = count
        self.data = data


def get_card_data_by_name(card):
    for set_card in set1:
        if set_card["name"].lower() == card.lower():
            return set_card
    for set_card in set2:
        if set_card["name"].lower() == card.lower():
            return set_card
    return None


def get_card_data_by_code(card):
    for set_card in set1:
        if set_card["cardCode"] == card:
            return set_card
    for set_card in set2:
        if set_card["cardCode"] == card:
            return set_card
    return None


with open('data/lor/set1-en_us.json') as f:
    set1 = json.load(f)
with open('data/lor/set2-en_us.json') as f:
    set2 = json.load(f)
