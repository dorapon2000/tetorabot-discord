import jpholiday

OTSUKARE_TIME = '17:30'


def isOtsukareTime(dt):
    return dt.strftime('%H:%M') == OTSUKARE_TIME and _isBizDay(dt)


def _isBizDay(dt):
    '''平日なら1を返す
    https://qiita.com/hid_tanabe/items/3c5e6e85c6c65f7b38be
    '''
    return dt.weekday() < 5 and not jpholiday.is_holiday(dt)


async def say(channel):
    await channel.send('今日もお仕事おつかれさま〜！')


async def reply(message):
    reply = f'{message.author.mention} おつかれ〜'
    await message.channel.send(reply)
