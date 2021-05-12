import os
import discord
import command_dispatcher
from dotenv import load_dotenv
from time import sleep


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print(f'{client.user} is connected to the following guilds:')
    for guild in client.guilds:
        print(f'\n{guild.name}(id: {guild.id})')
        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    response = None
    pause = 0
    if "TROLL" in message.content.upper():
        response = "http://dd.b.pvp.net/2_5_0/set3/en_us/img/cards/03FR002.png"
    if "NINJA" in message.content.upper():
        pause = 2
        response = "left\n\n\nand right\n\n\nand kick it to the side\n\n\nwe're going round\n\n\nand round\n\n\nand down to the ground\n\n\ngo\n\n\nyou got it\n\n\ngo go you got it"
    if len(message.content) > 0 and message.content[0] == '!':
        words = message.content.split()
        command = words[0][1:]
        args = words[1:]
        print(f"Handling command: {command} with args: {args}")
        response = command_dispatcher.dispatch(command, args)
    if response is not None:
        print(f"Responding with: {response}")
        if '\n\n\n' in response:
            responses = response.split('\n\n\n')
            for resp in responses:
                await message.channel.send(resp)
                sleep(pause)
        else:
            await message.channel.send(response)


def remove_mentions(message):
    content = message.content
    print(f"Content before replacing: {content}")
    for mention in message.mentions:
        if mention.id == client.user.id:
            content = content.replace(f'<@!{mention.id}>', '')
        else:
            content = content.replace(f'<@!{mention.id}>', mention.name)
    print(f"Content after replacing: {content}")
    return content


def run():
    print("Starting Discord bot")
    client.run(TOKEN)
