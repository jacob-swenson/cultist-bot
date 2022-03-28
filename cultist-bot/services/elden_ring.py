from services.models import elden_ring_models


def weapon(name):
    print('Getting weapon: ' + name)
    data = elden_ring_models.get_data('weapons', name)
    response = data['image'] + '\n\n\n'
    response += 'Name: ' + data['name'] + '\n'
    response += 'Category: ' + data['category'] + '\n'
    response += 'Weight: ' + str(data['weigth']) + '\n\n'
    response += 'Description\n```' + data['description'] + '```\n'
    response += 'Attack\n```'
    for attack_stat in data['attack']:
        response += attack_stat['name'] + ':\t' + str(attack_stat['amount']) + '\n'
    response += '```\n'
    response += 'Defence\n```'
    for defence_stat in data['defence']:
        response += defence_stat['name'] + ':\t' + str(defence_stat['amount']) + '\n'
    response += '```\n'
    response += 'Scales With\n```'
    for scale_stat in data['scalesWith']:
        response += scale_stat['name'] + ':\t' + scale_stat['scaling'] + '\n'
    response += '```\n'
    response += 'Required Attributes\n```'
    for required_stat in data['requiredAttributes']:
        response += required_stat['name'] + ':\t' + str(required_stat['amount']) + '\n'
    response += '```\n'
    return response


def item(name):
    print('Getting Item ' + name)
    data = elden_ring_models.get_data('items', name)
    response = data['image'] + '\n\n\n'
    response += 'Name: ' + data['name'] + '\n'
    response += 'Type: ' + data['type'] + '\n'
    response += 'Description\n```' + data['description'] + '```\n'
    response += 'Effect\n```' + data['effect'] + '```\n'
    return response


def shield(name):
    print('Getting Shield ' + name)
    data = elden_ring_models.get_data('shields', name)
    response = data['image'] + '\n\n\n'
    response += 'Name: ' + data['name'] + '\n'
    response += 'Category: ' + data['category'] + '\n'
    response += 'Weight: ' + str(data['weigth']) + '\n\n'
    response += 'Description\n```' + data['description'] + '```\n'
    response += 'Attack\n```'
    for attack_stat in data['attack']:
        response += attack_stat['name'] + ':\t' + str(attack_stat['amount']) + '\n'
    response += '```\n'
    response += 'Defence\n```'
    for defence_stat in data['defence']:
        response += defence_stat['name'] + ':\t' + str(defence_stat['amount']) + '\n'
    response += '```\n'
    response += 'Scales With\n```'
    for scale_stat in data['scalesWith']:
        response += scale_stat['name'] + ':\t' + scale_stat['scaling'] + '\n'
    response += '```\n'
    response += 'Required Attributes\n```'
    for required_stat in data['requiredAttributes']:
        response += required_stat['name'] + ':\t' + str(required_stat['amount']) + '\n'
    response += '```\n'
    return response


def ashes(name):
    print('Getting Ashes ' + name)
    data = elden_ring_models.get_data('ashes', name)
    response = data['image'] + '\n\n\n'
    response += 'Name: ' + data['name'] + '\n'
    response += 'Affinity: ' + data['affinity'] + '\n'
    response += 'Skill: ' + data['skill'] + '\n'
    response += 'Description:\n```' + data['description'] + '```\n'
    return response


def boss(name):
    print('Getting Boss ' + name)
    data = elden_ring_models.get_data('bosses', name)
    response = data['image'] + '\n\n\n'
    response += 'Name: ' + data['name'] + '\n'
    response += 'Location: ' + data['location'] + '\n'
    response += 'Description:\n```' + data['description'] + '```\n'
    response += 'Drops:\n```'
    for drop in data['drops']:
        response += drop + '\n'
    response += '```\n'
    return response


def npc(name):
    print('Getting NPC ' + name)
    data = elden_ring_models.get_data('npcs', name)
    response = data['image'] + '\n\n\n'
    response += 'Name: ' + data['name'] + '\n'
    response += 'Location: ' + data['location'] + '\n'
    response += 'Role: ' + data['role'] + '\n'
    response += 'Quote:\n```' + data['quote'] + '```\n'
    return response


def location(name):
    print('Getting Location ' + name)
    data = elden_ring_models.get_data('locations', name)
    response = data['image'] + '\n\n\n'
    response += 'Name: ' + data['name'] + '\n'
    response += 'Description:\n```' + data['description'] + '```\n'
    return response


def spirit(name):
    print('Getting Spirit ' + name)
    data = elden_ring_models.get_data('spirits', name)
    response = data['image'] + '\n\n\n'
    response += 'Name: ' + data['name'] + '\n'
    response += 'Description:\n```' + data['description'] + '```\n'
    response += 'FP Cost: ' + data['fpCost'] + '\n'
    response += 'HP Cost: ' + data['hpCost'] + '\n'
    return response


def talisman(name):
    print('Getting Talisman ' + name)
    data = elden_ring_models.get_data('talismans', name)
    response = data['image'] + '\n\n\n'
    response += 'Name: ' + data['name'] + '\n\n'
    response += 'Effect:\n```' + data['effect'] + '```\n'
    response += 'Description:\n```' + data['description'] + '```\n'
    return response


def armor(name):
    print('Getting Armor ' + name)
    data = elden_ring_models.get_data('armors', name)
    response = data['image'] + '\n\n\n'
    response += 'Name: ' + data['name'] + '\n'
    response += 'Category: ' + data['category'] + '\n'
    response += 'Weight: ' + str(data['weigth']) + '\n\n'
    response += 'Description:\n```' + data['description'] + '```\n'
    response += 'Damage Negation:\n```'
    for negation in data['dmgNegation']:
        response += negation['name'] + ': ' + str(negation['amount']) + '\n'
    response += '```\n'
    response += 'Resistance:\n```'
    for resistance in data['resistance']:
        response += resistance['name'] + ': ' + str(resistance['amount']) + '\n'
    response += '```\n'
    return response


def creature(name):
    print('Getting Creature: ' + name)
    data = elden_ring_models.get_data('creatures', name)
    response = data['image'] + '\n\n\n'
    response += 'Name: ' + data['name'] + '\n'
    response += 'Location: ' + data['location'] + '\n'
    response += 'Description:\n```' + data['description'] + '```\n'
    response += 'Drops:\n```'
    for drop in data['drops']:
        response += drop + '\n'
    response += '```\n'
    return response


def classes(name):
    print('Getting Class: ' + name)
    data = elden_ring_models.get_data('classes', name)
    response = data['image'] + '\n\n\n'
    response += 'Name: ' + data['name'] + '\n'
    response += 'Description:\n```' + data['description'] + '```\n'
    response += 'Stats:\n```'
    for stat in data['stats'].keys():
        response += stat + ': ' + data['stats'][stat] + '\n'
    response += '```\n'
    return response


def incantation(name):
    print('Getting Incantation: ' + name)
    data = elden_ring_models.get_data('incantations', name)
    response = data['image'] + '\n\n\n'
    response += 'Name: ' + data['name'] + '\n'
    response += 'Type: ' + data['type'] + '\n'
    response += 'Cost: ' + str(data['cost']) + '\n'
    response += 'Slots: ' + str(data['slots']) + '\n\n'
    response += 'Effects:\n```' + data['effects'] + '```\n'
    response += 'Description:\n```' + data['description'] + '```\n'
    response += 'Requires:\n```'
    for require in data['requires']:
        response += require['name'] + ': ' + str(require['amount']) + '\n'
    response += '```\n'
    return response


def sorcery(name):
    print('Getting Sorcery: ' + name)
    data = elden_ring_models.get_data('sorceries', name)
    response = data['image'] + '\n\n\n'
    response += 'Name: ' + data['name'] + '\n'
    response += 'Type: ' + data['type'] + '\n'
    response += 'Cost: ' + str(data['cost']) + '\n'
    response += 'Slots: ' + str(data['slots']) + '\n\n'
    response += 'Effects:\n```' + data['effects'] + '```\n'
    response += 'Description:\n```' + data['description'] + '```\n'
    response += 'Requires:\n```'
    for require in data['requires']:
        response += require['name'] + ': ' + str(require['amount']) + '\n'
    response += '```\n'
    return response


def ammo(name):
    print('Getting Ammo: ' + name)
    data = elden_ring_models.get_data('ammos', name)
    response = data['image'] + '\n\n\n'
    response += 'Name: ' + data['name'] + '\n'
    response += 'Type: ' + data['type'] + '\n\n'
    response += 'Description:\n```' + data['description'] + '```\n'
    response += 'Passive:\n```' + data['passive'] + '```\n'
    response += 'Attack Power:\n```'
    for attack in data['attackPower']:
        response += attack['name'] + ': ' + str(attack['amount']) + '\n'
    response += '```\n'
    return response

