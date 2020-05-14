import os
import discord
import ghoul_dispatcher
import command_dispatcher
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print(f'{client.user} is connected to the following guild:')
    for guild in client.guilds:
        print(f'\n{guild.name}(id: {guild.id})')
        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    response = None
    if message.content[0] == '!':
        words = message.content.split()
        command = words[0][1:]
        args = words[1:]
        print(f"Handling command: {command} with args: {args}")
        response = command_dispatcher.dispatch(command, args)
    elif str(message.channel.type) == "private":
        content = remove_mentions(message)
        print(f"Handling private message: {content}")
        response = ghoul_dispatcher.dispatch(content, str(message.author.id))
    else:
        for mention in message.mentions:
            if mention.id == client.user.id:
                content = remove_mentions(message)
                print(f"Handling mention: {content}")
                response = ghoul_dispatcher.dispatch(content, str(message.author.id))
                break
    if response is not None:
        print(f"Responding with: {response}")
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
