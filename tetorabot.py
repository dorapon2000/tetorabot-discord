import os
import re
import discord

from src import weather

TOKEN = os.environ['DISCORD_APP_TOKEN']
client = discord.Client()


@client.event
async def on_ready():
    print('tetorabot is ready')


@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == '/neko':
        await message.channel.send('にゃーん')
    elif message.content == '/wan':
        await message.channel.send('わお～ん')
    elif re.match('^/tenki[\s　][^\s　]+$', message.content):
        city = re.match('^/tenki[\s　]([^\s　]+)$', message.content).group(1)
        if city.isalpha() or weather.is_japanese(city):
            await weather.reply_weather(message, city)


client.run(TOKEN)
