import os
import re
from datetime import datetime
from pytz import timezone
import discord
from discord.ext import tasks

from src import weather
from src import otsukare
from src import thank_you

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

    elif message.mentions and re.search('/(otsukare|otukare)$', message.content):
        await otsukare.reply_to(message)

    elif message.content in ['/otsukare', '/otukare']:
        await otsukare.reply(message)

    elif (client.user in message.mentions and 'ありがと' in message.content
          or message.content in ['/arigatou', '/thanks', '/thankyou']):
        await thank_you.reply(message)

    elif re.match('^/tenki[\s　][^\s　]+$', message.content):
        city = re.match('^/tenki[\s　]([^\s　]+)$', message.content).group(1)
        if city.isalpha() or weather.is_japanese(city):
            await weather.reply_weather(message, city)


@tasks.loop(seconds=60)
async def loop():
    now = datetime.now(timezone('Asia/Tokyo'))
    if otsukare.isOtsukareTime(now):
        channel = client.get_channel(CHANNEL_ID)
        await otsukare.say(channel)


loop.start()
client.run(TOKEN)
