import os
import re
import ghoul_dispatcher
import command_dispatcher
from dotenv import load_dotenv
from slack import RTMClient, rtm
import slack


load_dotenv()
TOKEN = os.getenv('SLACK_TOKEN')
user_regex = re.compile(r'<@\w+>')
user_id = None


@RTMClient.run_on(event="Hello")
def connected(**payload):
    print("I'm on!")


@RTMClient.run_on(event="message")
async def say_hello(**payload):
    print(payload)
    data = payload['data']
    web_client = payload['web_client']
    if 'text' not in data:
        return
    if 'subtype' in data and data['subtype'] == 'bot_message':
        return
    message = remove_mentions(data['text'])
    response = None
    channel_id = data['channel']
    await rtm_client.typing(channel=channel_id)
    if message[0] is '/':
        words = message.split()
        command = words[0][1:]
        args = words[1:]
        print(f"Handling command: {command} with args: {args}")
        response = command_dispatcher.dispatch(command, args)
    else:
        print(f"Handling plain text: {message}")
        response = ghoul_dispatcher.dispatch(message)
    if response is not None:
        print(f"Responding with: {response}")
        web_client.chat_postMessage(
            channel=channel_id,
            text=response
        )


def remove_mentions(content):
    print(f"Content before replacing: {content}")
    content = user_regex.sub('', content).strip()
    print(f"Content after replacing: {content}")
    return content


def run():
    print("Starting Slack Bot")
    rtm_client.start()


rtm_client = RTMClient(token=TOKEN)
