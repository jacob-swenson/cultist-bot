import discord_bot
import slack_bot
import sys


if __name__ == "__main__":
    print(f"Running with args: {sys.argv}")
    slack = False
    for arg in sys.argv:
        if arg == "slack":
            slack = True
    if slack:
        slack_bot.run()
    else:
        discord_bot.run()
