from discord.ext import commands
from models import Deck, get_card_data_by_name, get_card_data_by_code


class LegendsOfRuneterra(commands.Cog):
    def __init__(self, bot, max_images=2):
        self.bot = bot
        self._last_member = None
        self.MAX_RELATED_IMAGES = max_images

    @commands.command(name='deck', help='Prints the decklist from an encoded deck')
    async def deck_code(self, ctx, code):
        print("Decoding deck: " + code)
        deck = Deck(code)
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
        await ctx.send(response)

    @commands.command(name='card', help='Displays card image')
    async def card(self, ctx, *kwargs):
        card = ' '.join(kwargs)
        print(f'Looking up card {card}')
        data = get_card_data_by_name(card)
        if data is None:
            print(f"Didn't find card {card}")
            await ctx.send(f"Card {card} not found!")
            return
        response = ""
        for image in data["assets"]:
            response += image["gameAbsolutePath"] + "\n"
        count = 0
        for associated_card in data["associatedCardRefs"]:
            if count == self.MAX_RELATED_IMAGES:
                break
            associated_data = get_card_data_by_code(associated_card)
            for image in associated_data["assets"]:
                response += image["gameAbsolutePath"] + "\n"
            count += 1
        await ctx.send(response)
