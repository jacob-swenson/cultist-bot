from services import ghoul, cthulhuwars, lor, base_service, user_service, rpg_service
import command_dispatcher
import json


def dispatch(req: str, uid: str):
    resp = ghoul.say(req)
    user = user_service.get_user(uid)
    node = user.get_node()
    intent = ghoul.get_intent(resp)
    if intent == 'cancel':
        user.set_node(None)
        return base_service.respond_to('_cancel')
    elif node is not None:
        return nodes[node](resp, uid)
    else:
        return intents[intent](resp, uid)


def draft(resp: json, uid: str):
    print("Ghoul thinks the user wants to run a draft")
    user = user_service.get_user(uid)
    players = []
    if 'contact' not in ghoul.get_entities(resp):
        user.set_node('draft')
        return base_service.respond_to('_draft_failed')
    for player in ghoul.get_entities(resp)["contact"]:
        players.append(player["value"])
    return cthulhuwars.draft(players)


def card(resp: json, uid: str):
    entities = ghoul.get_entities(resp)
    if 'contact' not in entities:
        print("Ghoul thinks the user wants to look up a card but didn't find a card name. Falling back to unknown")
        return base_service.respond_to('unknown')
    card_name = entities['contact'][0]['value']
    print(f"Ghoul thinks the user wants to look up the card {card_name}")
    return lor.card(card_name)


def unknown(resp: json, uid: str):
    print("Ghoul doesn't know what the user wants")
    return base_service.respond_to(ghoul.get_intent(resp))


def introduction(resp: json, uid: str):
    user = ghoul.get_entities(resp)['contact'][0]['value']
    return base_service.introduction(user)


def status(resp: json, uid: str):
    entities = ghoul.get_entities(resp)
    if 'sentiment' not in entities:
        print("Ghoul sees a status with no sentiment, assuming neutral")
        sentiment = 'neutral'
    else:
        sentiment = entities['sentiment'][0]['value']

    print("Ghoul thinks the user is giving their status")
    user_status = '_status_' + sentiment
    return base_service.respond_to(user_status)


def base_command(resp: json, uid: str):
    print("Handling base command")
    return base_service.respond_to(ghoul.get_intent(resp))


def populate_base_commands():
    for command in base_service.messages:
        if command == 'unknown':
            continue
        intents[command] = base_command


intents = {
    'draft': draft,
    'card': card,
    'unknown': unknown,
    'introduction': introduction,
    'status': status,
    'help': command_dispatcher.get_help,
    'generate_name': rpg_service.name_generator
}

nodes = {
    'get_gender': rpg_service.get_gender,
    'get_setting': rpg_service.get_setting,
    'draft': draft
}

populate_base_commands()
