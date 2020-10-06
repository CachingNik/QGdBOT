from discord.ext import commands
import os


client = commands.Bot(command_prefix=">")


client.load_extension("fts.meme")
client.load_extension("fts.voice")
client.load_extension("fts.filter")


@client.event
async def on_ready():
    channel = client.get_channel(760587314207522826)
    await channel.send("🟢 ONLINE")
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


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        await ctx.send("❌ Access Denied")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ Access Denied")


@client.command()
@commands.has_permissions(administrator=True)
async def shutdown(ctx):
    print("Shutting Down...")
    await ctx.send("🔴 OFFLINE")
    await ctx.bot.logout()


client.run(os.getenv("TOKEN"))
