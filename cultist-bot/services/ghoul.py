import os
import json
from wit import Wit
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('WIT_TOKEN')
client = Wit(access_token=TOKEN)


def get_intent(wit_resp: json):
    if "intent" not in wit_resp["entities"]:
        return "unknown"
    entities = get_entities(wit_resp)
    intent = entities["intent"][0]["value"]
    if intent == "hello" and "contact" in entities:
        return "introduction"
    return intent


def get_entities(wit_resp: json):
    return wit_resp["entities"]


def say(req: str):
    print(f"User said {req}")
    resp = client.message(req)
    print(f"Ghoul thinks:\n{resp}")
    return resp
