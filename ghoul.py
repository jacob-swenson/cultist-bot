import os
import json
from wit import Wit
from dotenv import load_dotenv
from cthulhuwars import factions
import drafter
from random import random

load_dotenv()
TOKEN = os.getenv('WIT_TOKEN')
client = Wit(access_token=TOKEN)
i_dont_know = ["I don't know what your talking about", "Pardon?", "I'm sorry?"]


def get_intent(wit_resp: json):
    return wit_resp["entities"]["intent"][0]["value"]


def say(sentence: str):
    print(f"User said {sentence}")
    resp = client.message(sentence)
    print(f"Wit thinks:\n{resp}")
    return intent_map[get_intent(resp)](resp["entities"])


def draft(resp: json):
    print("Wit thinks the user wants to run a draft")
    players = []
    for player in resp["contact"]:
        players.append(player["value"])
    return drafter.beautify_draft(drafter.run_draft(factions.copy(), players))


def unknown(resp: json):
    print("Wit doesn't know what the user wants")
    return random.selection(i_dont_know)


intent_map = {
    'draft': draft,
    'unknown': unknown
}
