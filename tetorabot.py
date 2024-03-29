import os
import re
from datetime import datetime
from pytz import timezone
import discord
from discord.ext import tasks

from src import weather
from src import otsukare
from src import youre_welcome
from src import thank_you
from src import decorate_reply

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

    if message.content in ['/neko', '/nyan']:
        await message.channel.send('にゃーん')

    elif message.content in ['/wan', '/inu']:
        await message.channel.send('わお～ん')

    elif message.mentions and re.search('/(otsukare|otukare|otsu|otu)', message.content):
        await otsukare.reply_to(message)

    elif re.search('/(otsukare|otukare|otsu|otu|taikin)|taikin', message.content):
        await otsukare.reply(message)

    elif (client.user in message.mentions and re.search('(/(arigato|thanks|thankyou)|ありがと)', message.content)
          or re.search('^/(arigatou?|thanks|thankyou)$', message.content)):
        await youre_welcome.reply(message)

    elif message.mentions and re.search('/(arigato|thanks|thankyou)', message.content):
        await thank_you.reply_to(message)

    elif re.match('^/tenki[\s　][^\s　]+$', message.content):
        city = re.match('^/tenki[\s　]([^\s　]+)$', message.content).group(1)
        if city.isalpha() or weather.is_japanese(city):
            await weather.reply_weather(message, city)

    elif re.match('^[^\s　]+[\s　の]天気$', message.content):
        city = re.match('^([^\s　]+)[\s　の]天気$', message.content).group(1)
        if city.isalpha() or weather.is_japanese(city):
            await weather.reply_weather(message, city)

    elif re.search('ふ[えぇ]+', message.content):
        user_name = message.author.name
        await message.channel.send(f'わあ！{user_name}が幼女になっちゃった！？')

    elif re.search('/(deco|hey)', message.content):
        await decorate_reply.reply_to(message)


@tasks.loop(seconds=60)
async def loop():
    now = datetime.now(timezone('Asia/Tokyo'))
    if otsukare.isOtsukareTime(now):
        channel = client.get_channel(CHANNEL_ID)
        # await otsukare.say(channel)


loop.start()
client.run(TOKEN)
