import discord_bot
import slack_bot
import sys


if __name__ == "__main__":
    print(f"Running with args: {sys.argv}")
    for arg in sys.argv:
        if arg == "slack":
            slack_bot.run()
    discord_bot.run()
