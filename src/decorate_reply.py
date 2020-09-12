import random


def choose_emoticon():
    emoticons = list(
        '💤😴🙂🤑✋😪🛌😎😤😒😙😏😳😌❗❓🤔😜💦'
        '💔😱😰😭😓😣😖😥😢❗😄😆😚😘😚💕💗😍😁😋😂😊🎵'
    )
    return random.choice(emoticons)


def choose_hello():
    hellos = (
        'hey❗',
        'YO❗',
        'うぉおおお',
        '起きて❗',
        'お❗❗',
        'よっよっ'
    )
    return random.choice(hellos)


def choose_special():
    special = (
        '金は命より重い',
        'ここ進研ゼミでやったとこだ❗❗',
        '相手の人は一般人です',
    )
    return random.choice(special)


async def reply_to(message):
    mentions = [user.mention for user in message.mentions]

    reply = ' '.join(mentions) + ' '
    for _ in range(random.randint(15, 30)):
        r = random.randint(0, 100)
        if 30 < r:
            reply += choose_emoticon()
        if 20 < r:
            reply += random.choice(mentions)
        elif 1 < r:
            reply += choose_hello()
        else:
            reply += choose_special()

    await message.channel.send(reply)
