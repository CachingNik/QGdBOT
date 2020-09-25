import discord
from discord.ext import commands
import praw
import random
import os


r = praw.Reddit(client_id=os.getenv("CLIENT_ID"),
                client_secret=os.getenv("CLIENT_SECRET"),
                password=os.getenv("PASSWORD"),
                user_agent="QGdBOT",
                username="CachingNik")


class Meme(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meme(self, ctx, *, topic=""):
        sr = r.subreddit(topic + "memes")
        ts = []
        t = sr.top(limit=30)

        for s in t:
            ts.append(s)

        rs = random.choice(ts)
        name = rs.title
        url = rs.url

        em = discord.Embed(title=name, color=discord.Colour.green())
        em.set_image(url=url)

        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(Meme(bot))
