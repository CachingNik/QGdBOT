import discord
from discord.ext import commands
import os
import praw
import random

r = praw.Reddit(client_id=os.getenv("CLIENT_ID"),
                client_secret=os.getenv("CLIENT_SECRET"),
                password=os.getenv("PASSWORD"),
                user_agent="QGdBOT",
                username="CachingNik")


client = commands.Bot(command_prefix=">")
bad_words = ["fuck", "shit"]
laughter = ["lol", "lel"]


@client.event
async def on_ready():
    print("Bot is ready")


@client.event
async def on_message(msg):
    for word in bad_words:
        if word in msg.content.lower():
            await msg.channel.send("Hey :rage: Mind your language!!!")
            await msg.delete()

    emoji1 = discord.utils.get(client.emojis, name='PepeLaugh')
    emoji2 = discord.utils.get(client.emojis, name='FRec')
    emoji3 = discord.utils.get(client.emojis, name='FakeBlob')

    for word in laughter:
        if word in msg.content.lower():
            await msg.channel.send(str(emoji1))

    if msg.content.lower() == "f":
        await msg.channel.send(str(emoji2))
        await msg.add_reaction("💔")

    if "nkli" in msg.content.lower():
        await msg.channel.send(str(emoji3))
        await msg.channel.send("Same to U")

    if "sed" in msg.content.lower():
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


@client.command()
async def meme(ctx, *, topic=""):
    sr = r.subreddit(topic + "memes")
    ts = []
    t = sr.top(limit=5)

    for s in t:
        ts.append(s)

    rs = random.choice(ts)
    name = rs.title
    url = rs.url

    em = discord.Embed(title=name, color=discord.Colour.green())
    em.set_image(url=url)

    await ctx.send(embed=em)


client.run(os.getenv("TOKEN"))
