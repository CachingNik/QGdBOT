import discord
import os
from discord.ext import commands
import youtube_dl


class Voice(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def cog_before_invoke(self, ctx):
        if ctx.message.author.voice is None:
            await ctx.send("ERROR ‼️: " + str(ctx.message.author.mention) + " absent from Voice Channel.")
            return

    @commands.command()
    @commands.has_any_role("🎵audio")
    async def join(self, ctx):
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
    @commands.has_any_role("🎵audio")
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
    @commands.has_any_role("🎵audio")
    async def play(self, ctx, url=""):
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

        if url == "":
            print("No URL")
            await ctx.send("Bhai link to dede play karne ke liye!!")
            return

        song_there = os.path.isfile("song.mp3")
        if song_there:
            os.remove("song.mp3")
            print("Removed old song file")

        ydl_opts = {
            'format': 'bestaudio/best',
            'noplaylist': True,
            'playlist_items': '0',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                dict_meta = ydl.extract_info(url, download=False)
                if '_type' in dict_meta.keys():
                    print("Search/Playlist")
                    await ctx.send("Plis provide a Video URL")
                    return
            except Exception as e:
                print(e)
                await ctx.send("Invalid URL")
                return
            if int(dict_meta['filesize']) > 15728640:
                print("Large File")
                await ctx.send("Very Large File 💩")
                return
            print("Downloading audio now")
            await ctx.send("Loading...")
            ydl.download([url])

        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                print("Renamed file " + str(file))
                os.rename(file, "song.mp3")

        vc.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda x: print(dict_meta['title'] + " Finished playing"))
        vc.source = discord.PCMVolumeTransformer(vc.source)
        vc.source.volume = 0.3

        await ctx.send("▶️ Now Playing: " + dict_meta['title'])
        print("Playing")

    @commands.command(pass_context=True)
    @commands.has_any_role("🎵audio")
    async def pause(self, ctx):
        vc = ctx.message.guild.voice_client

        if vc and vc.is_paused():
            print("Harkate")
            await ctx.send("Kitni baar pause krega??")
            return

        if vc and vc.is_playing():
            print("Pausing...")
            vc.pause()
            await ctx.send("⏸  Paused")
        else:
            print("Music not playing to pause")
            await ctx.send("Nothing is being played U Idiot")

    @commands.command(pass_context=True)
    @commands.has_any_role("🎵audio")
    async def resume(self, ctx):
        vc = ctx.message.guild.voice_client

        if vc and vc.is_playing():
            print("Harkate")
            await ctx.send("😒")
            return

        if vc and vc.is_paused():
            print("Resuming...")
            vc.resume()
            await ctx.send("▶  Resumed")
        else:
            print("Music not playing to resume")
            await ctx.send("Nothing is being played U Idiot")

    @commands.command(pass_context=True)
    @commands.has_any_role("🎵audio")
    async def stop(self, ctx):
        vc = ctx.message.guild.voice_client

        if vc and (vc.is_playing() or vc.is_paused()):
            print("Stopping...")
            vc.stop()
            await ctx.send("⏹  Stopped")
        else:
            print("Music not playing to stop")
            await ctx.send("Nothing is being played U Idiot")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingAnyRole):
            await ctx.send("❌ Access Denied")


def setup(bot):
    bot.add_cog(Voice(bot))
