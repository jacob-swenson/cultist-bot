from discord.ext import commands
import random


class CthulhuWars(commands.Cog):
    @commands.command(name='draft', help='Runs a Cthulhu Wars draft')
    async def draft(self, ctx, *kwargs):
        result = {player: [] for player in kwargs}
        factions = ['Opener of the Way', 'Crawling Chaos', 'Yellow Sign', 'Great Cthulhu', 'Sleepers', 'The Ancients',
                    'Black Goat', 'Windwalkers', 'Tcho-Tcho']
        loops = len(factions) // len(result)
        print('Looping ' + str(loops) + ' times')
        # draft factions
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
        # Compile results
        response = '```\n'
        for player in result:
            response += player + '\n'
            n = 1
            for option in result[player]:
                response += '\t' + str(n) + '. ' + option + '\n'
                n += 1
            response += '\n'
        response += '```'
        await ctx.send(response)
