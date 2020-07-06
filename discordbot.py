import discord
import random
import time
import discord.ext
from discord.exe import commands
import os
import traceback


bot = commands.Bot(command_prefix="mu:", help_command=None)
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_ready():
    print("ログイン完了")
    
@bot.command()
async def test(ctx) :
    await ctx.send("こん")
    
bot.run(token)
