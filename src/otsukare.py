import random
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


def choose_line():
    lines = [
        # [セリフが出る重み（確率）, セリフ]
        [10, '今日もお仕事おつかれさま〜！'],
        [10, '今日もご苦労さま〜'],
        [3, '乙'],
        [3, 'べ、べつにあんたのためにお疲れなんて言ってあげないんだから！！'],
        [3, 'おつかれちゃん'],
        [3, 'ぉ...  おつかれ...///'],
        [3, 'お！つ！！カレー'],
        [3, 'おっつっつ！'],
        [3, 'おつかれ〜'],
        [3, 'おつかれ♡'],
        [3, 'おつかれにゃん'],
        [3, 'おつかれ！こんな日はラーメンよ！！'],
        [3, 'おちゅかれ'],
        [3, 'おつかれ？'],
        [3, '言ってあげないよん'],
        [3, 'おつかれさま！お風呂にする？ご飯にする？それとも...'],
        [1, 'おかえり〜'],
    ]
    weights = [line[0] for line in lines]

    choosed_line = random.choices(lines, weights=weights)[0]
    return choosed_line[1]


async def reply(message):
    otsukare = choose_line()
    reply = f'{message.author.mention} {otsukare}'
    await message.channel.send(reply)


async def reply_to(message):
    otsukare = choose_line()
    mentions = ' '.join([user.mention for user in message.mentions])
    reply = f'{mentions} {otsukare}'
    await message.channel.send(reply)
