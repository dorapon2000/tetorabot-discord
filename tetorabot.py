import os
import re
import datetime
import discord
from discord.ext import tasks

from src import weather
from src import otsukare

TOKEN = os.environ['DISCORD_APP_TOKEN']
CHANNEL_ID = int(os.environ['DISCORD_APP_OREROOM_ID'])
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


@tasks.loop(seconds=60)
async def loop():
    now = datetime.datetime.now()
    if otsukare.isOtsukareTime(now):
        channel = client.get_channel(CHANNEL_ID)
        await otsukare.say(channel)


loop.start()
client.run(TOKEN)
