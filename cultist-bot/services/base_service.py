import random
import json


def respond_to(intent: str):
    print('Handling base response')
    return random.choice(messages[intent])


def introduction(user: str):
    print("Handling an introduction")
    pre = random.choice(introductions['pre'])
    post = random.choice(introductions['post'])
    return f"{pre}{user}{post}"


with open('data/messages/messages-en_us.json') as f:
    messages = json.load(f)

with open('data/messages/introductions-en_us.json') as f:
    introductions = json.load(f)
