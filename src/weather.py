import re
import csv
import requests
import unicodedata


def is_japanese(string):
    """Return true if japanese
    https://minus9d.hatenablog.com/entry/2015/07/16/231608

    Args:
        string (str): string
    Returns:
        bool : true if string is japanese
    """
    for ch in string:
        name = unicodedata.name(ch)
        if "CJK UNIFIED" in name \
                or "HIRAGANA" in name \
                or "KATAKANA" in name:
            return True
    return False


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
        with open('data/id_city_table.csv', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if city == row[0]:
                    city_code = row[1]
                    break
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
