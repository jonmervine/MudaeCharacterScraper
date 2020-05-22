import discord
from discord.ext import commands
import re
import asyncio

# client = discord.Client()
bot = commands.Bot(command_prefix='%')


class Output:

    def write_to_file(self, file, text):
        print('Out putting text to: ' + file)

        f = open(file, "a")
        f.write(text)
        f.close()

        # open and read the file after the appending:
        # f = open("demofile2.txt", "r")
        # print(f.read())


class Parser:

    def parse_mudae_text(self):
        print('hello parser')


@bot.command(name='get')
async def _get(ctx, *, arg):
    print('called get command')
    print(ctx)
    print(arg)
    # await ctx.send('$imaawg-s {}'.format(' '.join(args)))
    # await ctx.send(arg)
    await ctx.send('$imaawg-s ' + arg)


@bot.event
async def on_ready():
    print('Logged on as', bot.user)


async def on_message(message):
    # don't respond to ourselves
    if message.author == bot.user:
        return

    if message.channel.type != discord.ChannelType.private:
        return

    print('We are doing something with text')
    print(message.content)
    output = Output()
    output.write_to_file("Lucky Star.txt", message.content)

    # await message.channel.send(message.content)

bot.add_listener(on_message, 'on_message')
bot.run('token here')



