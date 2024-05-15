# Last revised by: 5/142024

# code right now is from the tutorial here: 
# https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-python

import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# from: https://stackoverflow.com/questions/64148371/discord-bot-can-only-see-itself-and-no-other-users-in-guild
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

client.run(TOKEN)

# Copyright of ThienTran Le 2024