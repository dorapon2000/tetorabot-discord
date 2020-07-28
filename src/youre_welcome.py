import random


def choose_line():
    lines = [
        # [セリフが出る重み（確率）, セリフ]
        [10, 'どういたしまして～'],
        [10, 'どういたまして'],
        [3, 'えへへ///'],
        [3, 'よかったぁ～'],
        [3, 'こっちこそありがと～'],
        [3, 'やった～！'],
        [3, 'べ、べつに嬉しくなんてないんだからね！'],
        [3, 'う、嬉しくなんてないもん！'],
        [1, 'うっす～'],
        [1, 'うす'],
    ]
    weights = [line[0] for line in lines]

    choosed_line = random.choices(lines, weights=weights)[0]
    return choosed_line[1]


async def reply(message):
    thank_you = choose_line()
    reply = f'{thank_you}'
    await message.channel.send(reply)
