import discord
import os
import requests
import json
from youtube import getSuggestedVideo


musicBots = ['Chip#4145', 'Hydra#1214']
suggestionHooks = ['ch!p'] # messages which activate song suggestion
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


def extractVideoId(url):
    # adapted for bots' messages format, but also works for normal links
    # it appears that every video id has 11 digits, but can not be sure 
    return url.partition("youtube.com/watch?v=")[-1].partition(")")[0]


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if str(message.author) in musicBots:
        try:
            for embed in message.embeds:
                embeddedMessage = embed.description
                if "youtube.com/watch?v=" in embeddedMessage:
                    ytId = extractVideoId(embeddedMessage)
                    suggestedVideoURL = getSuggestedVideo(ytId)
                    if suggestedVideoURL:
                        await message.channel.send("Suggested Youtube video: " + suggestedVideoURL)
        except Exception as error:
            print("Something went bad:", error)
    
    if message.content.startswith('!suggest'):
        ytId = extractVideoId(message.content)
        suggestedVideoURL = getSuggestedVideo(ytId)
        await message.channel.send("Suggested Youtube video: " + suggestedVideoURL)

    if message.content.startswith('!testbot'):
        await message.channel.send('Hello, I am here!') 


client.run(os.environ['TOKEN'])

