import discord
from discord.ext import commands
from pymongo import MongoClient
import os


cluster = MongoClient(os.getenv("DB"))
db = cluster["QG_Data"]
l_words = db["laughter"]
b_words = db["bad_words"]
k_words = db["k_words"]


class Filter(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):

        emoji1 = discord.utils.get(self.bot.emojis, name='PepeLaugh')
        emoji2 = discord.utils.get(self.bot.emojis, name='FRec')
        emoji3 = discord.utils.get(self.bot.emojis, name='FakeBlob')
        emoji4 = discord.utils.get(self.bot.emojis, name='Noob')

        swords = msg.content.lower().split(" ")

        if swords[0] == '>add' or swords[0] == '>rem':
            return

        lw = 0
        nw = 0
        fw = 0
        abuse = 0

        for word in swords:
            my_query = {"Word": word}
            if b_words.count_documents(my_query) != 0:
                await msg.channel.send("Hey " + str(msg.author.mention) + " :rage: Mind your language!!!")
                await msg.delete()
                abuse = 1

        if abuse == 0:
            for word in swords:
                my_query = {"Word": word}
                if l_words.find(my_query).count() > 0:
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

            if lw == 0:
                for word in swords:
                    my_query = {"Word": word}
                    if k_words.count_documents(my_query) != 0:
                        await msg.add_reaction("👍")

    @commands.command()
    @commands.has_any_role("🤴🏻leader", "💂‍sidekick")
    async def add(self, ctx, w_type="", word=""):

        if w_type == "":
            await ctx.send("Please mention a filter category (`laugh`, `bad`, `ok`).")
            return

        if word == "":
            await ctx.send("Add karne ke liye word toh de bhai.")
            return

        post = {"Word": word}

        if w_type == "laugh":
            if l_words.find().count() == 20:
                await ctx.send("Max limit reached!!")
                return
            if l_words.find(post).count() > 0:
                await ctx.send("👊, Bhag yaha se")
                return
            l_words.insert_one(post)
        elif w_type == "bad":
            if b_words.find().count() == 20:
                await ctx.send("Max limit reached!!")
                return
            if b_words.find(post).count() > 0:
                await ctx.send("👊, Bhag yaha se")
                return
            b_words.insert_one(post)
        elif w_type == "ok":
            if k_words.find().count() == 5:
                await ctx.send("Max limit reached!!")
                return
            if k_words.find(post).count() > 0:
                await ctx.send("👊, Bhag yaha se")
                return
            k_words.insert_one(post)
        else:
            await ctx.send("No such category exist.")
            return

        await ctx.send("✅ Done")
        print("New Word Added")

    @commands.command()
    @commands.has_any_role("🤴🏻leader", "💂‍sidekick")
    async def rem(self, ctx, w_type="", word=""):

        if w_type == "":
            await ctx.send("Please mention a filter category (`laugh`, `bad`, `ok`).")
            return

        if word == "":
            await ctx.send("Gadhe, remove kya karu??")
            return

        my_query = {"Word": word}

        if w_type == "laugh":
            if l_words.find(my_query).count() > 0:
                l_words.delete_one(my_query)
            else:
                await ctx.send("🚫 Word not found.")
                return
        elif w_type == "bad":
            if b_words.find(my_query).count() > 0:
                b_words.delete_one(my_query)
            else:
                await ctx.send("🚫 Word not found.")
                return
        elif w_type == "ok":
            if k_words.find(my_query).count() > 0:
                k_words.delete_one(my_query)
            else:
                await ctx.send("🚫 Word not found.")
                return
        else:
            await ctx.send("No such category exist.")
            return

        await ctx.send("✅ Done")
        print("Word Removed")

    @commands.command()
    async def filist(self, ctx):
        l_list = "\n".join(word['Word'] for word in l_words.find())
        b_list = "\n".join(word['Word'] for word in b_words.find())
        k_list = "\n".join(word['Word'] for word in k_words.find())

        if l_list == "":
            l_list = "-"
        if b_list == "":
            b_list = "-"
        if k_list == "":
            k_list = "-"

        embed = discord.Embed(title="List of Filtered words", color=discord.Color.dark_gold())
        embed.add_field(name="LAUGH", value=l_list, inline=True)
        embed.add_field(name="BAD", value=b_list, inline=True)
        embed.add_field(name="OK", value=k_list, inline=True)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Filter(bot))
