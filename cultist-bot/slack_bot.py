import os
import ghoul_dispatcher
import command_dispatcher
from dotenv import load_dotenv
from slack import RTMClient


load_dotenv()
TOKEN = os.getenv('SLACK_TOKEN')


@RTMClient.run_on(event="message")
def say_hello(**payload):
    print(payload)
    data = payload['data']
    web_client = payload['web_client']
    if 'text' not in data:
        return

    if 'Hello' in data['text']:
        channel_id = data['channel']
        thread_ts = data['ts']
        user = data['user']

        web_client.chat_postMessage(
            channel=channel_id,
            text=f"Hi <@{user}>!"
        )


def run():
    print("Starting Slack Bot")
    rtm_client = RTMClient(token=TOKEN)
    rtm_client.start()
