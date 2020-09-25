import discord
import os
from discord.ext import commands
import youtube_dl


class Voice(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_any_role("leader", "sidekick")
    async def join(self, ctx):
        if ctx.message.author.voice is None:
            await ctx.send("Brather, U need to join a Voice Channel first.")
            return

        channel = ctx.message.author.voice.channel
        vc = ctx.message.guild.voice_client

        if vc and vc.is_connected():
            if ctx.voice_client.channel == channel:
                await ctx.send("😒 Already in your channel BRO")
            else:
                await vc.move_to(channel)
                await ctx.send("✅ Moved to " + str(channel) + " Channel")
        else:
            await channel.connect()
            await ctx.send("✅ Joined " + str(channel) + " Channel")

    @commands.command()
    @commands.has_any_role("leader", "sidekick")
    async def leave(self, ctx):
        channel = ctx.message.author.voice.channel
        vc = ctx.message.guild.voice_client
        if vc and vc.is_connected():
            if vc.is_playing():
                vc.stop()
            await vc.disconnect()
            await ctx.send("❎ Left " + str(channel) + " Channel")
        else:
            await ctx.send("Abee Noob, leave karvane ke liye pehle join toh karva")

    @commands.command(pass_context=True)
    @commands.has_any_role("leader", "sidekick")
    async def play(self, ctx, url):
        guild = ctx.message.guild
        channel = ctx.message.author.voice.channel
        vc = ctx.message.guild.voice_client

        if vc and vc.is_connected():
            if ctx.voice_client.channel != channel:
                await vc.move_to(channel)
                await ctx.send("✅ Moved to " + str(channel) + " Channel")
        else:
            await ctx.send("BRO!! 😡😡 I m not connected to a voice channel")
            return

        if vc.is_playing():
            print("Already playing")
            await ctx.send("Let this song finish first or Pause/Stop it!!")
            return

        song_there = os.path.isfile("song.mp3")
        if song_there:
            os.remove("song.mp3")
            print("Removed old song file")

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
            'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
        }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                dict_meta = ydl.extract_info(url, download=False)
            except Exception as e:
                print(e)
                await ctx.send("Invalid URL")
                return
            if int(dict_meta['filesize']) > 20971520:
                print("Large File")
                await ctx.send("Very Large File 💩")
                return
            print("Downloading audio now")
            ydl.download([url])

        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                sname = file
                print("Renamed file " + str(file))
                os.rename(file, "song.mp3")

        nsname = sname.split("-", 2)
        vc.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print(nsname[0] + " Finished playing"))
        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 0.07

        await ctx.send("Playing: " + nsname[0])
        print("Playing")

    @commands.command(pass_context=True)
    @commands.has_any_role("leader", "sidekick")
    async def pause(self, ctx):
        vc = ctx.message.guild.voice_client

        if vc and vc.is_playing():
            print("Pausing...")
            vc.pause()
            await ctx.send("Audio Paused")
        else:
            print("Music not playing to pause")
            await ctx.send("Nothing is being played U Noob")

    @commands.command(pass_context=True)
    @commands.has_any_role("leader", "sidekick")
    async def resume(self, ctx):
        vc = ctx.message.guild.voice_client

        if vc and vc.is_paused():
            print("Resuming...")
            vc.resume()
            await ctx.send("Audio Resumed")
        else:
            print("Music not playing to resume")
            await ctx.send("Nothing is being played U Noob")

    @commands.command(pass_context=True)
    @commands.has_any_role("leader", "sidekick")
    async def stop(self, ctx):
        vc = ctx.message.guild.voice_client

        if vc and vc.is_playing():
            print("Stopping...")
            vc.stop()
            await ctx.send("Audio Stopped")
        else:
            print("Music not playing to stop")
            await ctx.send("Nothing is being played U Noob")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingAnyRole):
            await ctx.send("❌ Access Denied")


def setup(bot):
    bot.add_cog(Voice(bot))
