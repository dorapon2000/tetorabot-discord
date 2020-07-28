import random


def choose_line():
    lines = [
        # [セリフが出る重み（確率）, セリフ]
        [10, 'ありがとう！'],
        [3, 'ありがとー'],
        [3, 'どうも、ありがとうね'],
        [3, 'いつも、助かってるよ！ありがとう！'],
        [3, '私からもお礼を言うね！ありがとう！'],
        [1, '謝謝!'],
        [1, 'شُكْرًا'],
        [1, 'thx!'],
        [1, '🍆'],
        [1, '(本当はありがとうなんて思ってない)'],
    ]
    weights = [line[0] for line in lines]

    choosed_line = random.choices(lines, weights=weights)[0]
    return choosed_line[1]


async def reply_to(message):
    thank_you = choose_line()
    mentions = ' '.join([user.mention for user in message.mentions])
    reply = f'{mentions} {thank_you}'
    await message.channel.send(reply)
