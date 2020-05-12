from services.models import lor_models

MAX_RELATED_IMAGES = 2


def deck_code(code):
    print("Decoding deck: " + code)
    deck = lor_models.Deck(code)
    response = "```\n"
    first = True
    for champion in deck.champions:
        if not first:
            response += " / "
        response += champion
        first = False
    response += "\n"
    for region, cards in deck.cards_by_region.items():
        response += "\n" + region + "\n-----------\n"
        for card in cards:
            response += "\t" + str(card.count) + ": " + card.data["name"] + "\n"
    response += "```"
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


