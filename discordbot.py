from discord.ext import commands
import os
import time
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.command()
async def ping(ctx):
  starttime = time.time()
  msg = await ctx.send("測定中")
  ping = time.time() - starttime
  await msg.edit(content=str(ping))


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

    
 


bot.run(token)
