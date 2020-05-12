import os
import discord

TOKEN = os.environ['DISCORD_APP_TOKEN']
client = discord.Client()
client.run(TOKEN)


@client.event
async def on_ready():
    print('tetorabot is ready')


@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == '/neko':
        await message.channel.send('にゃーん')
