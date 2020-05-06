from discord.ext import commands
from drafter import run_draft, beautify_draft

factions = ['Opener of the Way', 'Crawling Chaos', 'Yellow Sign', 'Great Cthulhu', 'Sleepers', 'The Ancients',
            'Black Goat', 'Windwalkers', 'Tcho-Tcho']


class CthulhuWars(commands.Cog):
    @commands.command(name='draft', help='Runs a Cthulhu Wars draft')
    async def draft(self, ctx, *kwargs):
        result = run_draft(factions, kwargs)
        response = beautify_draft(result)
        await ctx.send(response)
