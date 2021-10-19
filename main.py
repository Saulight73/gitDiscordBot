import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv(dotenv_path="config")

client = commands.Bot(command_prefix='*')

@client.command(name='join',pass_context = True)
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()


client.run(os.getenv("TOKEN"))


