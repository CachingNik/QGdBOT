#import discord
from discord.ext import commands

client = commands.Bot(command_prefix=">")
bad_words = ["fuck", "F", "FUCK", "f"]

@client.event
async def on_ready():
    print("Bot is ready")


@client.event
async def on_message(msg):
    for word in bad_words:
        if word in msg.content:
            await msg.channel.send("Hey :rage: Mind your language!!!")
            await msg.delete()

    await client.process_commands(msg)


@client.command(aliases=["Hi", "Yo"])
async def hello(ctx):
    await ctx.send("Hi Brather")


@client.command(aliases=["sc"])
@commands.has_permissions(administrator=True)
async def sourcecode(ctx):
    await ctx.send("https://github.com/CachingNik/QGdBOT")


client.run("<- Token goes here ->")
