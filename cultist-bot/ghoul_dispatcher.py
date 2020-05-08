from services import ghoul, cthulhuwars, lor, base_service
import command_dispatcher
import json


def dispatch(req: str):
    resp = ghoul.say(req)
    intent = ghoul.get_intent(resp)
    return intents[intent](resp)


def draft(resp: json):
    print("Ghoul thinks the user wants to run a draft")
    players = []
    for player in ghoul.get_entities(resp)["contact"]:
        players.append(player["value"])
    return cthulhuwars.draft(players)


def card(resp: json):
    entities = ghoul.get_entities(resp)
    if 'contact' not in entities:
        print("Ghoul thinks the user wants to look up a card but didn't find a card name. Falling back to unknown")
        return base_service.respond_to('unknown')
    card_name = entities['contact'][0]['value']
    print(f"Ghoul thinks the user wants to look up the card {card_name}")
    return lor.card(card_name)


def unknown(resp: json):
    print("Ghoul doesn't know what the user wants")
    return base_service.respond_to(ghoul.get_intent(resp))


def introduction(resp: json):
    user = ghoul.get_entities(resp)['contact'][0]['value']
    return base_service.introduction(user)


def status(resp: json):
    entities = ghoul.get_entities(resp)
    if 'sentiment' not in entities:
        print("Ghoul sees a status with no sentiment, cannot compute")
        return base_service.respond_to('unknown')

    print("Ghoul thinks the user is giving their status")
    user_status = 'status_' + entities['sentiment'][0]['value']
    return base_service.respond_to(user_status)


def base_command(resp: json):
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
    'help': command_dispatcher.get_help
}

populate_base_commands()
