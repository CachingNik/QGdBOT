import discord
from discord.ext import commands

client = commands.Bot(command_prefix=">")


@client.event
async def on_ready():
    print("Bot is ready")


@client.command(aliases=["Hi", "Yo"])
async def hello(ctx):
    await ctx.send("Hi Brather")

client.run("<- Token goes here ->")
