import discord
from discord.ext import commands
import os


client = commands.Bot(command_prefix=">")


client.load_extension("fts.meme")
client.load_extension("fts.voice")
client.load_extension("fts.filter")


@client.event
async def on_ready():
    print("Bot is ready")


@client.command(aliases=["Hi", "Yo", "yo", "Hola"])
async def hello(ctx):
    await ctx.send("Hi Brather")


@client.command(aliases=["Bye", "Sayonara", "sayonara"])
async def bye(ctx):
    await ctx.send("Bye Brather")


@client.command(aliases=["sc"])
@commands.has_permissions(administrator=True)
async def sourcecode(ctx):
    await ctx.send("https://github.com/CachingNik/QGdBOT")


client.run(os.getenv("TOKEN"))
