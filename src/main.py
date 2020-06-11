import discord

from src.mudae import Mudae

client = discord.Client()


@client.event
async def on_ready():
    print('Logged on as', client.user)


@client.event
async def on_message(message):
    if message.author == client.user or message.channel.name != 'mudaescraping':
        return

    if message.author.name == 'DarkMage530':
        mudae.handle_my_message(message)

    if message.author.id == 582107046435094531:
        if message.embeds:
            mudae.handle_message(message.embeds[0])
        else:
            mudae.handle_non_embed_message(message)


@client.event
async def on_message_edit(before, after):
    # If from Mudae, and before/after are different, and in the scraping channel
    if after.author.id == 582107046435094531 and before.embeds[0].description != after.embeds[0].description \
            and after.channel.name == 'mudaescraping':
        mudae.handle_message_edit(after.embeds[0])


mudae = Mudae()
client.run('derpyderp')
