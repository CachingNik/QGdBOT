import discord
from discord.ext import commands
import os


client = commands.Bot(command_prefix=">")
bad_words = ["fuck", "shit", "gay"]
laughter = ["lol", "lel", "lmao", "lul", "rofl"]


client.load_extension("fts.meme")
client.load_extension("fts.voice")


@client.event
async def on_ready():
    print("Bot is ready")


@client.event
async def on_message(msg):
    for word in bad_words:
        if word in msg.content.lower():
            await msg.channel.send("Hey " + str(msg.author.mention) + " :rage: Mind your language!!!")
            await msg.delete()

    emoji1 = discord.utils.get(client.emojis, name='PepeLaugh')
    emoji2 = discord.utils.get(client.emojis, name='FRec')
    emoji3 = discord.utils.get(client.emojis, name='FakeBlob')
    emoji4 = discord.utils.get(client.emojis, name='Noob')

    swords = msg.content.lower().split(" ")

    lw = 0
    nw = 0
    fw = 0

    for word in laughter:
        if word in swords:
            await msg.channel.send(str(emoji1))
            lw = 1

    if "nkli" in swords:
        await msg.channel.send(str(emoji3))
        await msg.channel.send("Same to U")
        fw = 1

    if "noob" in swords:
        await msg.channel.send(str(emoji4))
        nw = 1

    if "f" in swords:
        if lw == 0 and fw == 0 and nw == 0:
            await msg.channel.send(str(emoji2))
            await msg.add_reaction("💔")

    if "sed" in swords:
        await msg.add_reaction("😭")

    await client.process_commands(msg)


@client.command(aliases=["Hi", "Yo"])
async def hello(ctx):
    await ctx.send("Hi Brather")


@client.command(aliases=["Bye", "Sayonara"])
async def bye(ctx):
    await ctx.send("Bye Brather")


@client.command(aliases=["sc"])
@commands.has_permissions(administrator=True)
async def sourcecode(ctx):
    await ctx.send("https://github.com/CachingNik/QGdBOT")


client.run(os.getenv("TOKEN"))
