import os
import re
import requests
import discord

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
    elif re.match('^/tenki[\s　][a-zA-Z]+$', message.content):
        city = re.match('^/tenki[\s　]([a-zA-Z]+)$', message.content).group(1)
        await reply_weather(message, city)


async def reply_weather(message, city):
    """Replay weather forecast
    http://weather.livedoor.com/weather_hacks/webservice

    Args:
        message (discord.message): Message
        city (str): City
    """
    if city == 'hamamatsu' or city == 'hamamatu':
        city_code = '220040'
    elif city == 'shizuoka' or city == 'sizuoka':
        city_code = '220010'
    elif city == 'nagoya':
        city_code = '230010'
    elif city == 'toukyou':
        city_code = '130010'
    elif city == 'hakodate':
        city_code = '017010'
    elif city == 'sapporo':
        city_code = '016010'
    else:
        await message.channel.send('都市名が有効じゃないよ～ん')
        return

    url = f'http://weather.livedoor.com/forecast/webservice/json/v1?city={city_code}'
    res = requests.get(url).json()

    public_month = res['publicTime'][5:7]
    public_day = res['publicTime'][8:10]
    public_oclock = res['publicTime'][11:13]

    reply = f"""[天気予報]
{res['title']} ({public_month}/{public_day} {public_oclock}時 時点)
@ {res['link']}

{res['forecasts'][0]['dateLabel']} : {res['forecasts'][0]['telop']}
{res['forecasts'][1]['dateLabel']} : {res['forecasts'][1]['telop']}
---
{res['copyright']['title']}
"""

    await message.channel.send(reply)


client.run(TOKEN)
