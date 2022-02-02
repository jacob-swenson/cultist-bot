from services.models import lor_models

MAX_RELATED_IMAGES = 3


def deck_code(code):
    print("Decoding deck: " + code)
    deck = lor_models.Deck(code)
    response = code + "\n\n\n"
    response += "```\n"
    first = True
    for champion in deck.champions:
        if not first:
            response += " / "
        response += champion
        first = False
    response += "\n\n"
    first = True
    for region in deck.regions:
        if not first:
            response += " / "
        response += region
        first = False
    response += "\n"
    for card_type, cards in deck.cards_by_type.items():
        if len(cards) > 0:
            response += "\n" + card_type + "\n-----------\n"
            for card in cards:
                response += "\t" + str(card.count) + ": (" + str(card.data["cost"]) + ") " + card.data["name"] + "\n"
    response += "```"
    response += "\n\n\n"
    response += "<https://runeterra.ar/decks/code/" + code + ">"
    return response


def card(name):
    print(f'Looking up card_name {name}')
    data = lor_models.get_card_data_by_fuzzy_search(name)
    if data is None:
        print(f"Didn't find card_name {name}")
        return f"card {name} not found!"
    response = ""
    for image in data["assets"]:
        response += image["gameAbsolutePath"] + "\n"
    count = 0
    for associated_card in data["associatedCardRefs"]:
        if count == MAX_RELATED_IMAGES:
            break
        associated_data = lor_models.get_card_data_by_code(associated_card)
        for image in associated_data["assets"]:
            response += image["gameAbsolutePath"] + "\n"
        count += 1
    return response


def emote(name):
    print(f'Lookung up emote {name}')
    data = lor_models.get_emote_by_fuzzy_search(name)
    if data is None:
        print(f"Didn't find emote {name}")
        return lor_models.get_emote_names()
    return data["url"]

