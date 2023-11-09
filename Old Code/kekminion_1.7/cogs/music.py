import discord
from discord.ext import commands
import yt_dlp
import time
import queue

#python3 -m pip install -U yt-dlp
# ^^^ run when starting bot for the first time. ^^^
# ----------------------------------------
#https://github.com/ytdl-org/youtube-dl#output-template
# ^^^ tags for info reference ^^^

queue = []

YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
FFMPEG_OPTIONS = {
    'before_options':
    '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-vn'
}

global globalInfo

with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
    globalInfo = ydl.extract_info(
        'https://www.youtube.com/watch?v=jNQXAC9IVRw', download=False)
global uploaderSong
global uploaderIDSong
global requesterSong
global isLooping  #Makes current song loop or not.
global URL  #URL to the current song.
global songTitle  #Title of current song.
global songSeconds  #Seconds of current song.
global songLength  #Length of current song.
global songID  #ID of current song from link.


class music(commands.Cog):
    def __init__(self, client):
        self.client = client

# ---------------------------------------- Join Command ----------------------------------------
# Bot joins the voice channel of the author.

    @commands.command(aliases=['j', 'connect'])
    async def join(self, ctx):
        if ctx.author.voice and not ctx.voice_client:  # If the person is in a channel
            channel = ctx.author.voice.channel
            await channel.connect()
            await ctx.reply('Bot joined!', mention_author=False)
            print(f"Join command used, joining voice channel...")
        elif not ctx.author.voice:
            await ctx.reply(
                "You must be in a voice channel first so I can join it.",
                mention_author=False)
            print(f"Join command used, but could not join a voice channel.")
        elif ctx.voice_client:
            await ctx.reply("I'm already in a voice channel.",
                            mention_author=False)
            print(
                f"Join command used, but bot was already in a voice channel.")
        else:
            await ctx.reply(
                "You must be in a voice channel first so I can join it.",
                mention_author=False)
            print(f"Join command used, but could not join a voice channel.")

# ---------------------------------------- Leave Command ----------------------------------------
# Bot leave voice channel.

    @commands.command(aliases=['l', 'disconnect', 'd', 'dc'])
    async def leave(self, ctx):
        if ctx.voice_client and ctx.author.voice:  # If the bot is in a voice channel
            await ctx.guild.voice_client.disconnect()  # Leave the channel
            await ctx.reply('Bot left', mention_author=False)
            print(f"Leave command used, leaving voice channel...")
        elif not ctx.author.voice:
            await ctx.reply("You are not in a voice channel.",
                            mention_author=False)
            print(
                f"Leave command used, but author was not in a voice channel.")
        else:
            await ctx.reply(
                "I'm not in a voice channel, use the join command to make me join.",
                mention_author=False)
            print(
                f"Leave command used, but the bot was not in a voice channel.")

# ---------------------------------------- Play Command ----------------------------------------
# Bot plays audio from a YouTube link.

    @commands.command(aliases=['p', 'music', 'song'])
    async def play(self, ctx, url):
        if ctx.author.voice and not ctx.voice_client:  # If the person is in a channel.
            channel = ctx.author.voice.channel
            await channel.connect()
            await ctx.reply('Bot joined', mention_author=False)
            print(f"Play command used, joining voice channel...")
        if (ctx.author.voice):
            YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
            FFMPEG_OPTIONS = {
                'before_options':
                '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                'options': '-vn'
            }
            global voice
            voice = discord.utils.get(self.client.voice_clients,
                                      guild=ctx.guild)
            if not voice.is_playing(
            ) and ctx.voice_client:  #Makes sure bot isn't playing music and is in a voice channel.
                    await ctx.reply("Searching...", mention_author=False
                                    )  #Lets user know the command has started.
                    with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
                        info = ydl.extract_info(url, download=False)
                    uploaderSong = info['uploader']
                    uploaderIDSong = info['uploader_id']
                    requesterSong = ctx.message.author.id
                    isLooping = False  #Default is False.
                    isPaused = False  #Default is False.
                    URL = info['url']
                    songTitle = info['title']
                    songSeconds = info['duration']
                    songID = info['id']
                    global globalInfo
                    globalInfo = info
                    globalInfo['title'] = info['title']
                    if songSeconds >= 3600:  #Converts seconds to a stantard time format with hours.
                        songLength = time.strftime("%H:%M:%S",
                                                   time.gmtime(songSeconds))
                    elif songSeconds >= 60:  #Converts seconds to a stantard time format with no hours.
                        songLength = time.strftime("%M:%S",
                                                   time.gmtime(songSeconds))
                    else:  #Converts seconds to a stantard time format with hours.
                        songLength = time.strftime("%H:%M:%S",
                                                   time.gmtime(songSeconds))
                    voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
                    #voice.is_playing()
                    await ctx.send("Song Found!")
                    #queue.append(str("https://www.youtube.com/watch?v=" + songID))  #Lets user know the command has found the song.
                    embed = discord.Embed(
                        title="Playing ♪... ",
                        description=
                        f"Title: [`{songTitle}`](https://www.youtube.com/watch?v={songID}) \nDuration: `{songLength}` \nUploaded by: [`{str(uploaderSong)}`](https://www.youtube.com/{uploaderIDSong})",
                        color=0x44ff44)
                    if songID is None:  #If no ID, then default thumbnail.
                        songID = "https://www.designtagebuch.de/wp-content/uploads/mediathek/2017/08/youtube-logo.jpg"
                    else:  #Use song ID's thumbnail.
                        songID = info['id']
                    embed.set_image(
                        url=f"https://img.youtube.com/vi/{songID}/0.jpg".
                        format(songID=songID))
                    await ctx.send(embed=embed)
            elif voice.is_playing(
            ) and ctx.voice_client:  #Check if song is currently playing and if bot is in vc.
                embed = discord.Embed(
                    title="",
                    description=
                    f"A song is already playing! \n Adding song to queue... \n {url} \n WARNING: The queue has no function right now, this is just a test.",
                    color=0x44ff44)
                await ctx.reply(embed=embed, mention_author=False)
                print(
                    f"Play command used, but a song was already playing. Queueing the requested song..."
                )
                queue.append(url)
            else:
                embed = discord.Embed(
                    title="",
                    description=f"Unknown error playing requested song!",
                    color=0xff3c28)
                await ctx.reply(embed=embed, mention_author=False)

        elif (ctx.voice_client is None):
            await ctx.reply(
                "You must be in a voice channel first so I can play it.",
                mention_author=False)
            print(f"Play command used, but bot was not in a voice channel.")
        elif (ctx.author_voice is None):
            await ctx.reply(
                "You must be in a voice channel first so I can play it.",
                mention_author=False)
            print(f"Play command used, but bot was not in a voice channel.")
        else:
            await ctx.reply("Bot is already playing", mention_author=False)
            print(f"Play command used, but bot was already playing music.")
            return

# ---------------------------------------- Resume Command ----------------------------------------
# Resumes audio from Bot, assuming Bot was already paused.

    @commands.command(aliases=['r', 'continue'])
    async def resume(self, ctx):
        global isPaused
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if ctx.voice_client and ctx.author.voice:
            if not voice.is_playing() and isPaused:
                voice.resume()
                await ctx.reply('Song is resuming...', mention_author=False)
                isPaused = False
                print(f"Resume command used, resuming music...")
            elif voice.is_playing() and not isPaused:
                await ctx.send('Song is already playing.',
                               mention_author=False)
                print(
                    f"Resume command used, but the music was already playing.")
            else:
                await ctx.reply('There is no song playing.',
                                mention_author=False)
                print(f"Resume command used, but there is no song playing.")
        elif not ctx.voice_client:
            await ctx.reply("Bot is not in a voice channel.",
                            mention_author=False)
            print(f"Resume command used, but bot is not in a voice channel.")
        elif not ctx.author.voice:
            await ctx.reply("You are not in a voice channel.",
                            mention_author=False)
            print(
                f"Resume command used, but author is not in a voice channel.")
        else:
            await ctx.reply('There is no song playing.', mention_author=False)
            print(f"Resume command used, but there is no song playing.")

# ---------------------------------------- Pause Command ----------------------------------------
# Pauses audio playing from Bot.

    @commands.command(aliases=['pa'])
    async def pause(self, ctx):
        print("testpause")
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if ctx.voice_client and ctx.author.voice:
            if voice.is_playing():
                voice.pause()
                await ctx.reply('Song has been paused', mention_author=False)
                global isPaused
                isPaused = True
                print(f"Pause command used, paused music.")
            elif isPaused:
                print("is paused now")
                await ctx.reply('Song is already paused.',
                                mention_author=False)
                print(f"Pause command used, but the music was already paused.")
            else:
                await ctx.reply('There is no song playing.',
                                mention_author=False)
                print(f"Pause command used, but there is no song playing.")
        elif not ctx.voice_client:
            await ctx.reply("Bot is not in a voice channel.",
                            mention_author=False)
            print(f"Pause command used, but bot is not in a voice channel.")
        elif not ctx.author.voice:
            await ctx.reply("You are not in a voice channel.",
                            mention_author=False)
            print(f"Pause command used, but author is not in a voice channel.")
        else:
            await ctx.reply('There is no song playing.', mention_author=False)
            print(f"Pause command used, but there is no song playing.")

# ---------------------------------------- Stop Command ----------------------------------------
# Stops the music from playing.

    @commands.command(aliases=['st'])
    async def stop(self, ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)

        if voice.is_playing() and ctx.voice_client:
            voice.stop()
            await ctx.reply('Stopped', mention_author=False)
            print(f"Stop command used, song is stopping...")
        elif not ctx.voice_client:
            await ctx.reply('You are not in a voice channel.',
                            mention_author=False)
            print(f"Stop command used, but author is not in a voice channel.")
        else:
            await ctx.reply('There is not song playing.', mention_author=False)
            print(f"Stop command used, but there is no song playing.")

# ---------------------------------------- Test Command ----------------------------------------
# Shows information of the current song.

    @commands.command()
    async def test3(self, ctx):
        print(f"--------------------- Status: ")

# ---------------------------------------- Now Playing Command ----------------------------------------
# Shows information of the current song.

    @commands.command(aliases=['np', 'now', 'nowplaying', 'now playing'])
    async def now_playing(self, ctx):
        uploaderSong = globalInfo['uploader']
        uploaderIDSong = globalInfo['uploader_id']
        requesterSong = ctx.message.author.id
        songTitle = globalInfo['title']
        songSeconds = globalInfo['duration']
        songID = globalInfo['id']
        if ctx.voice_client:
            if songSeconds >= 3600:
                songLength = time.strftime("%H:%M:%S",
                                           time.gmtime(songSeconds))
            elif songSeconds >= 60:
                songLength = time.strftime("%M:%S", time.gmtime(songSeconds))
            else:
                songLength = time.strftime("%H:%M:%S",
                                           time.gmtime(songSeconds))
            if voice.is_playing() or voice.is_paused():
                if requesterSong is not None:
                    embed = discord.Embed(
                        title="Now Playing ♪... ",
                        description=
                        f"Title: [`{songTitle}`](https://www.youtube.com/watch?v={songID}) \nDuration: `{songLength}` \nUploaded by: [`{str(uploaderSong)}`](https://www.youtube.com/{uploaderIDSong}) \nRequested By: <@{requesterSong}>",
                        color=0x44ff44)
                    embed.set_image(
                        url=f"https://img.youtube.com/vi/{songID}/0.jpg".
                        format(songID=songID))
                    await ctx.reply(embed=embed, mention_author=False)
                    print(
                        f"Now Playing command used, showing current song information..."
                    )
                else:
                    embed = discord.Embed(
                        title="Now Playing ♪... ",
                        description=
                        f"Title: [`{songTitle}`](https://www.youtube.com/watch?v={songID}) \nDuration: `{songLength}` \nUploaded by: [`{str(uploaderSong)}`](https://www.youtube.com/{uploaderIDSong}) \nRequested By: `Unknown`",
                        color=0x44ff44)
                    embed.set_image(
                        url=f"https://img.youtube.com/vi/{songID}/0.jpg".
                        format(songID=songID))
                    await ctx.reply(embed=embed, mention_author=False)
                    print(
                        f"Now Playing command used, showing current song information..."
                    )
                    print(f"--------------------- Status: ")
            else:
                embed = discord.Embed(title="",
                                      description=f"There is no song playing.",
                                      color=0xff3c28)
                await ctx.reply(embed=embed, mention_author=False)
                print(
                    f"Now Playing command used, but there is no song playing.")
        else:
            await ctx.reply("There is no song playing.", mention_author=False)
            print(f"Now Playing command used, but there is no song playing.")

# ---------------------------------------- Queue Command ----------------------------------------
# Shows the queue of songs.

    @commands.command(aliases=['q'])
    async def queue(self, ctx):
        if queue is None:
            queue.clear()
            embed = discord.Embed(
                title="",
                description=
                f"There are no items in the queue! \n WARNING: The queue has no function right now, this is just a test.",
                color=0xff3c28)
            await ctx.reply(embed=embed, mention_author=False)
        elif queue is not None:
            embed = discord.Embed(
                title="",
                description=
                f"{queue} \n WARNING: The queue has no function right now, this is just a test.",
                color=0x44ff44)
            await ctx.reply(embed=embed, mention_author=False)
        else:
            embed = discord.Embed(
                title="",
                description=
                f"There are no items in the queue! \n WARNING: The queue has no function right now, this is just a test.",
                color=0xff3c28)
            await ctx.reply(embed=embed, mention_author=False)


# ---------------------------------------- Clear Command ----------------------------------------
# Clears queue of songs.

    @commands.command(aliases=['c', 'clearqueue'])
    async def clear(self, ctx):
        if queue is None:
            queue.clear()
            embed = discord.Embed(
                title="",
                description=
                f"Queue is already empty! \n WARNING: The queue has no function right now, this is just a test.",
                color=0xff3c28)
            await ctx.reply(embed=embed, mention_author=False)
        elif queue is not None:
            queue.clear()
            embed = discord.Embed(
                title="",
                description=
                f"Queue cleared! \n WARNING: The queue has no function right now, this is just a test.",
                color=0x44ff44)
            await ctx.reply(embed=embed, mention_author=False)
        else:
            queue.clear()
            embed = discord.Embed(
                title="",
                description=
                f"Queue is already empty! \n WARNING: The queue has no function right now, this is just a test.",
                color=0xff3c28)
            await ctx.reply(embed=embed, mention_author=False)


async def setup(client):
    await client.add_cog(music(client))
