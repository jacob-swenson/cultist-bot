import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from lor import LegendsOfRuneterra
from cthulhuwars import CthulhuWars


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'{bot.user} is connected to the following guild:')
    for guild in bot.guilds:
        print(f'\n{guild.name}(id: {guild.id})')
        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}')


@bot.command(name='hello', help='Greeting')
async def hello(ctx):
    response = "Hello, I'm your friendly neighborhood cultist bot!"
    await ctx.send(response)


bot.add_cog(LegendsOfRuneterra(bot))
bot.add_cog(CthulhuWars(bot))
bot.run(TOKEN)
