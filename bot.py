import discord
from discord.ext import commands
import os


client = commands.Bot(command_prefix=">")


client.load_extension("fts.meme")
client.load_extension("fts.voice")
client.load_extension("fts.filter")


@client.event
async def on_ready():
    channel = client.get_channel(760066807854923796)
    des = "Hey guys!! This new update gives u the power to filter words into 3 diff " \
          "categories according to your choice. The diff reactions 😂😡 of the bot on these categories " \
          "is already known to u. U can either add or remove any word into any of these predefined category.\n" \
          "The 3 Categories are `LAUGH` `BAD` `OK`.\n\n" \
          "Commands:\n" \
          "1. To add word to a category: `>add [category] [word]`\n" \
          "2. To remove word from a category: `>rem [category] [word]`\n" \
          "3. To view the list of Filtered words: `>filist`\n\n" \
          "**PS: Only one word can be added or removed at a time using the commands.**"
    embed = discord.Embed(title="🆕 Update 🥳 (Filter Words)", description=des)
    embed.add_field(name="For more Info", value="https://github.com/CachingNik/QGdBOT")
    await channel.send(embed=embed)
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
