from services.drafter import run_draft, beautify_draft
from fuzzywuzzy import process
import json


def draft(players):
    result = run_draft(get_factions(), players)
    response = beautify_draft(result)
    return response


def get_factions():
    faction_names = []
    for faction in factions:
        faction_names.append(factions[faction]['name'])
    return faction_names


def get_faction_resources(name: str):
    response = ""
    for faction in factions:
        if factions[faction]['name'] == name:
            resources = factions[faction]
            response += resources['name'] + ' Resources:\n'
            response += 'Faction Sheet: ' + resources['sheet-image'] + '\n'
            response += 'Spellbooks: ' + resources['spells-image'] + '\n'
            response += 'Wiki: ' + resources['wiki'] + '\n'
            response += 'Strategy Video: ' + resources['youtube'] + '\n'
    return response


def summon_faction(name: str):
    requested_faction = process.extractOne(name, get_factions())
    print(f"Fuzzy Wuzzy is {requested_faction[1]}% sure the user is looking for {requested_faction[0]}")
    return get_faction_resources(requested_faction[0])


with open('data/cthulhu-wars/factions.json') as factions_input:
    factions = json.load(factions_input)
