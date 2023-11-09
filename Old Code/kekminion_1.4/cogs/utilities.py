import discord
from discord.ext import commands
import openai
import yt_dlp
import os

openai.api_key = "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"


class utilities(commands.Cog):
    def __init__(self, client):
        self.client = client

#python3 -m pip install -U yt-dlp
# ---------------------------------------- File Download Command ----------------------------------------
# Downloads a video / audio file from the link provided from the provided websites:
# ▫️ YouTube videos, playlists, and thumbnails
# ▫️ Soundcloud songs, playlists, and thumbnails
# ▫️ Twitch clips, VODS, and thumbnails
# ▫️ Twitter videos* and thumbnails*
# ▫️ Reddit videos** and thumbnails**
# ▫️ Facebook videos and thumbnails
# ▫️ Instagram videos and thumbnails
# ▫️ Pinterest videos*** and thumbnails***
# ▫️ VK videos and thumbnails
# ▫️ Cornhub videos
# ▫️ MySpace videos
#
# *You have to open the video, you can't use the "share" link.
# **You can copy only the post link.
# ***You must use the link shortener or "share" button.

    @commands.command(aliases=['v', 'vi', 'vid'])
    async def video(self, ctx, *, url: str = None):
        print("Video command used...")
        try:
            if 'soundcloud' in str(url):
                await ctx.reply("Must be a link to a video!",
                                mention_author=False)
            else:
                await ctx.reply("Downloading file...", mention_author=False)
                video_there = os.path.isfile("file.mov")
                if video_there:
                    os.remove("file.mov")

                ydl_opts = {
                    'format':
                    'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                    'videoformat':
                    "mp4",
                    'postprocessors': [{
                        'key': 'FFmpegVideoConvertor',
                        'preferedformat': 'mov',
                    }],
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                for file in os.listdir("./"):
                    if file.endswith(".mov"):
                        os.rename(file, "file.mov")
                video_there = os.path.isfile("file.mov")
                if video_there:
                    await ctx.channel.send('File Downloaded!',
                                           file=discord.File("file.mov"))
        except:
            await ctx.reply("Invalid link!", mention_author=False)

    @commands.command(aliases=['a', 'au', 'aud'])
    async def audio(self, ctx, *, url: str = None):
        print("Audio command used...")
        try:
            await ctx.reply("Downloading file...", mention_author=False)
            song_there = os.path.isfile("file.mp3")
            if song_there:
                os.remove("file.mp3")

            ydl_opts = {
                'format':
                'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            for file in os.listdir("./"):
                if file.endswith(".mp3"):
                    os.rename(file, "file.mp3")
            song_there = os.path.isfile("file.mp3")
            if song_there:
                await ctx.channel.send('File Downloaded!',
                                       file=discord.File("file.mp3"))
        except:
            await ctx.reply("Invalid link!", mention_author=False)


#https://stackoverflow.com/questions/71873182/no-module-named-openai
#    pip install openai
#https://platform.openai.com/account/api-keys
# ---------------------------------------- ChatGPT Command ----------------------------------------
# Uses ChatGPT AI to generate a message from the author.
'''
    @commands.command(aliases=['gpt', 'ai'])
    async def chatgpt(ctx, *args):
        print("test")
        input = [*args]
        await ctx.reply("Generating ChatGPT message...", mention_author=False)
        print("ChatGPT command used, generating message...")
        response = openai.Completion.create(model="text-davinci-003",
                                            prompt=input,
                                            temperature=0.5,
                                            max_tokens=100,
                                            top_p=1,
                                            frequency_penalty=1,
                                            presence_penalty=1,
                                            stop=[" Human:", " AI:"])
        text = response['choices'][0]['text']
        print("ChatGPT prompt: [", *args, "]")
        print("--------------------" + text + "\n--------------------")
        await ctx.reply(" " + text)
'''


async def setup(client):
    await client.add_cog(utilities(client))
