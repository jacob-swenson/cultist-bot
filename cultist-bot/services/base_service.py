import random
import json


def respond_to(intent: str):
    print('Handling base response')
    return random.choice(messages[intent])


def introduction(user: str):
    print("Handling an introduction")
    pre = random.choice(messages['_intro_pre'])
    post = random.choice(messages['_intro_post'])
    return f"{pre}{user}{post}"


with open('cultist-bot/data/messages/messages-en_us.json') as f:
    messages = json.load(f)
