# TetoraBot for discord

![tetorabot](https://github.com/dorapon2000/tetorabot-discord/blob/master/img/tetorabot_sample.png)

## Feature
- /neko : にゃーん
- /wan : わお～ん
- /thanks : どういたしまして
- @someone /thanks : @someone ありがとう
- /otsukare : @me おつかれさま
- @someone /otsukare : @someone おつかれさま
- /tenki [都市名] : 天気予報
- /hey @someone : 豪華なメンションになる

## How to install

1. Create a application in [discord dev. portal](https://discord.com/developers/applications) and you can get a token.
2. Add the bot into the server. (Requires admin)
3. Fork or clone this repository.
4. Deploy the bot somewhere (maybe heroku) with the token as environment variable.
5. Try some commands in discord channel where the bot installed.

## How to run in local for debug

```sh
git clone git@github.com:dorapon2000/tetorabot-discord.git
cd tetorabot-discord

# For pip
pip install -r requirements.txt

# For conda
conda create -n tetorabot
conda install requests
conda install pytz
pip install discord.py  # Does not exist in conda
pip install jpholiday  # Does not exist in conda

# Requires discord app token
export DISCORD_APP_TOKEN='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

# Run in local
python tetorabot.py

# Try some commands in discord channel where the bot installed.
```
