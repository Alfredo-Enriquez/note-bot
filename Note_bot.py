import discord
import os
import requests
from bs4 import BeautifulSoup
from discord.ext import commands

token = 'MTA3MzQxODY0NjI4NzgyNzAwNA.GAZZ_E.oB03jWwsoKm5btZj3yPgU4pnuz64Uu6W4AQnBg'

intents = discord.Intents.all() # or .all() if you ticked all, that is easier
intents.members = True # If you ticked the SERVER MEMBERS INTENT

#instantiate discord client
client = discord.Client(intents=intents)

# discord event to check when the bot is online
@client.event
async def on_ready():
    print(f'{client.user} is ready to go!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('~hello'):
        await message.channel.send('Yo!')

    if message.content.startswith('~rick'):
        await message.channel.send('Golly!')
        
    if message.content.startswith('~NASA'):
        await message.channel.send('My name is Rick and I work at NASA!')

client.run(token)