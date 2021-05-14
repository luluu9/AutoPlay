import discord
import os
import requests
import json
from youtube import getSuggestedVideo

musicBots = ["Chip#4145", "Hydra#1214"]
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if str(message.author) in musicBots:
        try:
            for embed in message.embeds:
                videoMessage = embed.description
                ytId = videoMessage.partition("youtube.com/watch?v=")[-1].partition(")")[0]
                suggestedVideoURL = getSuggestedVideo(ytId)
                if suggestedVideoURL:
                    await message.channel.send(".p " + suggestedVideoURL)

        except Exception as error:
            print("Something went bad:", error)
    
    if message.content.startswith('!testbots'):
        await message.channel.send('.help') 
        await message.channel.send('ch!help') 
      
client.run(os.environ['TOKEN'])

