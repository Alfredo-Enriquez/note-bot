import discord
import os
import requests
from bs4 import BeautifulSoup
from discord.ext import commands
from urllib.request import urlopen
from requests_html import AsyncHTMLSession

token = 'MTA3MzQxODY0NjI4NzgyNzAwNA.GioRAq.gr4vgypae3U4HQcxCeKL_Xmf09VtpT62TXuiW8'

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

    if message.content.startswith('~search drake nonstop'):
        search_term = message.content[8:]

        #replacing ' ' with '-' in search term
        search_term = search_term.replace(' ', '-')

        url_to_scrape = "https://genius.com/" + search_term + "-lyrics"

        page = requests.get(url_to_scrape)

        soup = BeautifulSoup(page.text, 'html.parser')

        #scraping for error message in html
        error = soup.find(string="Oops! Page not found")

        #if error is found
        if error == "Oops! Page not found":
            #replace '-' with '%20' for search url
            search_term = search_term.replace('-', '%20')
            url_to_scrape = "https://genius.com/search?q=" + search_term
            await message.channel.send(url_to_scrape)
        #if error is not found
        else:
            await message.channel.send(url_to_scrape)

    if message.content.startswith('~lyrics'):
        search_term = message.content[8:]
        search_term = search_term.replace(' ', '-')

        url_to_scrape = "https://genius.com/" + search_term + "-lyrics"

        page = requests.get(url_to_scrape)

        soup = BeautifulSoup(page.text, 'html.parser')

        error = soup.find(string="Oops! Page not found")

        if error == "Oops! Page not found":
            search_term = search_term.replace('-', '%20')
            search_url = "https://genius.com/search?q=" + search_term

            #page = requests.get(search_url)
            #soup = BeautifulSoup(page.text, 'html.parser')

            session = AsyncHTMLSession()
            r = await session.get(search_url)
            r.html.arender(sleep=5)

            soup = BeautifulSoup(r.html.raw_html, "html.parser")

            tags = soup.findAll("a")  # titles

            print(tags)

            session.close()
            
            await message.channel.send(search_url)
        else:
            await message.channel.send(url_to_scrape)

client.run(token)