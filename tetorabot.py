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
    elif message.content == '/wan':
        await message.channel.send('わお～ん')
    elif re.match('^/tenki[\s　][a-zA-Z]+$', message.content):
        city = re.match('^/tenki[\s　]([a-zA-Z]+)$', message.content).group(1)
        await reply_weather(message, city)


def convert_emoji(weather):
    w = re.sub('晴れ?', chr(int('2600', 16)), weather)
    w = re.sub('曇り?', chr(int('2601', 16)), w)
    w = w.replace('雨', chr(int('2602', 16)))
    w = w.replace('雷', chr(int('26A1', 16)))
    w = w.replace('雪', chr(int('2744', 16)))
    w = w.replace('のち', '→')
    w = w.replace('時々', '/')

    return w


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

    city = res['location']['city']
    today = res['forecasts'][0]['date'][5:].replace('-', '/')
    tommorow = res['forecasts'][1]['date'][5:].replace('-', '/')
    telop0 = convert_emoji(res['forecasts'][0]['telop'])
    telop1 = convert_emoji(res['forecasts'][1]['telop'])

    reply = f""">> {city}の天気
{today} : {telop0}
{tommorow} : {telop1}
"""

    await message.channel.send(reply)


client.run(TOKEN)
