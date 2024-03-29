from services import cthulhuwars, base_service, lor, elden_ring


def get_handler(command: str):
    if command not in commands:
        return unknown
    return commands[command]['handler']


def dispatch(command: str, args):
    return get_handler(command)(command, args)


def draft(command, players):
    print('User wants to run a Cthulhu Wars draft')
    return cthulhuwars.draft(players)


def summon(command, name_arr):
    name = ' '.join(name_arr)
    print(f'User wants to summon {name}')
    return cthulhuwars.summon_faction(name)


def card(command, name_arr):
    name = ' '.join(name_arr)
    print(f'User wants to look up the card {name}')
    return lor.card(name)


def emote(command, name_arr):
    name = ' '.join(name_arr)
    print(f'User wants to look up the emote {name}')
    return lor.emote(name)


def deck(command, code):
    if len(code) != 1:
        print(f"User didn't give a valid deckcode: {code}")
        return "Your input doesn't look correct. Please use format: " \
               "\n!deck CEBQCAQFAEAQCAJCBAAQKEA2DUUCWMJSGUBAEAQFAQFAEAIFDE4ACAQBAURS2"
    return lor.deck_code(code[0])


def weapon(command, name_arr):
    name = ' '.join(name_arr)
    print(f'User wants to look up the weapon {name}')
    return elden_ring.weapon(name)


def item(command, name_arr):
    name = ' '.join(name_arr)
    print(f'User wants to look up the item {name}')
    return elden_ring.item(name)


def shield(command, name_arr):
    name = ' '.join(name_arr)
    print(f'User wants to look up the shield {name}')
    return elden_ring.shield(name)


def ashes(command, name_arr):
    name = ' '.join(name_arr)
    print(f'User wants to look up the ashes {name}')
    return elden_ring.ashes(name)


def boss(command, name_arr):
    name = ' '.join(name_arr)
    print(f'User wants to look up the boss {name}')
    return elden_ring.boss(name)


def npc(command, name_arr):
    name = ' '.join(name_arr)
    print(f'User wants to look up the NPC {name}')
    return elden_ring.npc(name)


def location(command, name_arr):
    name = ' '.join(name_arr)
    print(f'User wants to look up the Location {name}')
    return elden_ring.location(name)


def spirit(command, name_arr):
    name = ' '.join(name_arr)
    print(f'User wants to look up the Spirit {name}')
    return elden_ring.spirit(name)


def talisman(command, name_arr):
    name = ' '.join(name_arr)
    print(f'User wants to look up the Talisman {name}')
    return elden_ring.talisman(name)


def armor(command, name_arr):
    name = ' '.join(name_arr)
    print(f'User wants to look up the Armor {name}')
    return elden_ring.armor(name)


def creature(command, name_arr):
    name = ' '.join(name_arr)
    print(f'User wants to look up the Creature {name}')
    return elden_ring.creature(name)


def incantation(command, name_arr):
    name = ' '.join(name_arr)
    print(f'User wants to look up the Incantation {name}')
    return elden_ring.incantation(name)


def sorcery(command, name_arr):
    name = ' '.join(name_arr)
    print(f'User wants to look up the Sorcery {name}')
    return elden_ring.sorcery(name)


def ammo(command, name_arr):
    name = ' '.join(name_arr)
    print(f'User wants to look up the Ammo {name}')
    return elden_ring.ammo(name)


def classes(command, name_arr):
    name = ' '.join(name_arr)
    print(f'User wants to look up the Class {name}')
    return elden_ring.classes(name)


def base_command(command, args):
    print('Handling base command')
    return base_service.respond_to(command)


def unknown(command, args):
    print(f'Unknown input: {command} with args: {args}')
    return base_service.respond_to('unknown')


def get_help(*kwargs):
    print('Showing help test')
    resp = 'I am a bot built by m3ddl3r as a side project in his free time.\n'
    resp += 'Commands cultist knows:\n```\n'
    for cmd in commands:
        if cmd[0] != '_':
            resp += f"{cmd}:\t{commands[cmd]['help']}\n"
    resp += '```'
    return resp


def populate_base_commands():
    for command in base_service.messages:
        if command == 'unknown':
            continue
        commands[command] = {
            'help': 'Basic text-response command',
            'handler': base_command
        }


commands = {
    'draft': {
        'help': 'Runs a draft for Cthulhu Wars',
        'handler': draft
    },
    'summon': {
        'help': 'Summon a Great Old One (see their faction information',
        'handler': summon
    },
    'card': {
        'help': 'Looks up a card from Legends of Runeterra',
        'handler': card
    },
    'emote': {
        'help': 'Looks up an emote',
        'handler': emote
    },
    'deck': {
        'help': 'Shows cards from a generated deck code',
        'handler': deck
    },
    'weapon': {
        'help': 'Looks up an Elden Ring Weapon',
        'handler': weapon
    },
    'ashes': {
        'help': 'Looks up an Ashes of War in Elend Ring',
        'handler': ashes
    },
    'item': {
        'help': 'Looks up an Elden Ring Item',
        'handler': item
    },
    'shield': {
        'help': 'Looks up an Elden Ring Shield',
        'handler': shield
    },
    'boss': {
        'help': 'Looks up an Elden Ring Boss',
        'handler': boss
    },
    'npc': {
        'help': 'Looks up an Elden Ring NPC',
        'handler': npc
    },
    'location': {
        'help': 'Looks up an Elden Ring Location',
        'handler': location
    },
    'spirit': {
        'help': 'Looks up an Elden Ring Spirit',
        'handler': spirit
    },
    'talisman': {
        'help': 'Looks up an Elden Ring Talisman',
        'handler': talisman
    },
    'armor': {
        'help': 'Looks up an Elden Ring Armor',
        'handler': armor
    },
    'creature': {
        'help': 'Look up an Elden Ring Creature',
        'handler': creature
    },
    'incantation': {
        'help': 'Look up an Elden Ring Incantation',
        'handler': incantation
    },
    'sorcery': {
        'help': 'Look up an Elden Ring Sorcery',
        'handler': sorcery
    },
    'ammo': {
        'help': 'Look up an Elden Ring Ammo',
        'handler': ammo
    },
    'class': {
        'help': 'Look up an Elden Ring Class',
        'handler': classes
    },
    'help': {
        'help': 'Displays this message',
        'handler': get_help
    }
}

populate_base_commands()
