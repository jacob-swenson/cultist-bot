import os
import random

import discord
import json
from dotenv import load_dotenv
from lor_deckcodes import LoRDeck, CardCodeAndCount

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print(f'{client.user} is connected to the following guild:\n')
    for guild in client.guilds:
        print(f'{guild.name}(id: {guild.id})')
        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(message.content)
    if message.content[0] == '!':
        words = message.content.split()
        command = words[0][1:]
        params = words[1:]
        await handle_command(message, command.lower(), params)


async def handle_command(message, command, params):
    print('Handling command: ' + command)
    cmd = commands.get(command, readme)
    await cmd(message, params)


async def readme(message, params):
    response = "Incantations I know:\n"
    for command in commands:
        response += "!" + command + "\n"
    await message.channel.send(response)


async def hello(message, params):
    response = "Hello, I'm your friendly neighborhood cultist bot!"
    await message.channel.send(response)


async def deckcode(message, params):
    if len(params) != 1:
        response = "Your incantation doesn't sound correct. To summon a deck list use format:\n" + \
                   "```!deck CEBAIAIFB4WDANQIAEAQGDAUDAQSIJZUAIAQCBIFAEAQCBAA```"
    else:
        print("Decoding deck: " + params[0])
        response = "```\n"
        deck = Deck(params[0])
        first = True
        for champion in deck.champions:
            if not first:
                response += " / "
            response += champion
            first = False
        response += "\n\n"
        for region, cards in deck.cards_by_region.items():
            response += region + "\n-----------\n"
            for card in cards:
                response += "\t" + str(card.count) + ": " + card.data["name"] + "\n"
        response += "```"
    await message.channel.send(response)


async def draft(message, params):
    result = {player: [] for player in params}
    factions = ['Opener of the Way', 'Crawling Chaos', 'Yellow Sign', 'Great Cthulhu', 'Sleepers', 'The Ancients',
                'Black Goat', 'Windwalkers', 'Tcho-Tcho']
    loops = len(factions) // len(result)
    print('Looping ' + str(loops) + ' times')
    for x in range(0, loops):
        print('Loop ' + str(x))
        for player in result:
            print('Handling player ' + player)
            print(factions)
            repeat = True
            attempts = 0
            timeout = 10
            while repeat:
                selected = random.choice(factions)
                if selected in result[player]:
                    repeat = True
                    if attempts is timeout:
                        result[player].append('N/A')
                        repeat = False
                else:
                    print('Chose ' + selected + ' for player ' + player)
                    result[player].append(selected)
                    factions.remove(selected)
                    repeat = False
    response = '```\n'
    for player in result:
        response += player + '\n'
        n = 1
        for option in result[player]:
            response += '\t' + str(n) + '. ' + option + '\n'
            n += 1
        response += '\n'
    response += '```'
    await message.channel.send(response)


class Deck:
    def __init__(self, code):
        deck = LoRDeck.from_deckcode(code)
        cards = []
        self.champions = []
        self.regions = []
        self.cards_by_region = {}
        for cardcode in deck:
            card = CardCodeAndCount.from_card_string(cardcode)
            if card.set == 1:
                cardset = set1
            elif card.set == 2:
                cardset = set2
            for set_card in cardset:
                if set_card["cardCode"] == cardcode[2:]:
                    if set_card["rarity"] == "Champion":
                        self.champions.append(set_card["name"])
                    if set_card["region"] not in self.regions:
                        self.regions.append(set_card["region"])
                        self.cards_by_region[set_card["region"]] = []
                    cards.append(Card(card.count, set_card))
                    self.cards_by_region[set_card["region"]].append(Card(card.count, set_card))
        self.cards = sorted(cards, key=lambda x: x.data["cost"])
        for k, v in self.cards_by_region.items():
            self.cards_by_region[k] = sorted(v, key=lambda x: x.data["cost"])


class Card:
    def __init__(self, count: int, data: json):
        self.count = count
        self.data = data


commands = {
    'draft': draft,
    'deckcode': deckcode,
    'hello': hello,
    'help': readme
}


with open('data/lor/set1-en_us.json') as f:
    set1 = json.load(f)
with open('data/lor/set2-en_us.json') as f:
    set2 = json.load(f)
client.run(TOKEN)
