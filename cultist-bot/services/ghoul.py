import os
import json
from wit import Wit
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('WIT_TOKEN')
client = Wit(access_token=TOKEN)
CONFIDENCE_THRESHOLD = float(os.getenv('WIT_CONFIDENCE_THRESHOLD'))
print("Ghoul is pruning all responses with confidence below " + str(CONFIDENCE_THRESHOLD))


def get_intent(wit_resp: json):
    if 'intent' not in wit_resp['entities']:
        return 'unknown'
    entities = get_entities(wit_resp)
    intent = entities['intent'][0]['value']
    if intent == 'hello' and 'contact' in entities:
        return 'introduction'
    return intent


def get_entities(wit_resp: json):
    return wit_resp['entities']


def prune_response(wit_resp: json):
    remove = []
    for entity in wit_resp['entities']:
        for i in range(0, len(wit_resp['entities'][entity])):
            if wit_resp['entities'][entity][i]['confidence'] < CONFIDENCE_THRESHOLD:
                del wit_resp['entities'][entity][i]
        if len(wit_resp['entities'][entity]) == 0:
            remove.append(entity)
    for entity in remove:
        wit_resp['entities'].pop(entity)


def say(req: str):
    print(f"Sending '{req}' to Ghoul")
    resp = client.message(req)
    print(f"Ghoul thinks:\n{resp}")
    prune_response(resp)
    print(f"After pruning response:\n{resp}")
    return resp
