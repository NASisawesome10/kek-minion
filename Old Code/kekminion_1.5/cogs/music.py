import discord
from discord.ext import commands
#import youtube_dl
import yt_dlp
#import os
import time
import queue

#python3 -m pip install -U yt-dlp
# ^^^ run when starting bot for the first time. ^^^
# ----------------------------------------
#https://github.com/ytdl-org/youtube-dl#output-template
# ^^^ tags for info reference ^^^

global queue


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
                try:
                    await ctx.reply("Searching...", mention_author=False
                                    )  #Lets user know the command has started.
                    with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
                        info = ydl.extract_info(url, download=False)
                    global uploaderSong
                    uploaderSong = info['uploader']
                    global uploaderIDSong
                    uploaderIDSong = info['uploader_id']
                    global requesterSong
                    requesterSong = ctx.message.author.id
                    global isLooping  #Makes current song loop or not.
                    isLooping = False  #Default is False.
                    global isSongActive
                    isSongActive = False
                    global isPaused  #Shows whether a song is paused or not.
                    isPaused = False  #Default is False.
                    global URL  #URL to the current song.
                    URL = info['url']
                    global songTitle  #Title of current song.
                    songTitle = info['title']
                    global songSeconds  #Seconds of current song.
                    songSeconds = info['duration']
                    global songLength  #Length of current song.
                    global songID  #ID of current song from link.
                    songID = info['id']
                    global songInfo  #Info of current song.
                    songInfo = info
                    if songSeconds >= 3600:  #Converts seconds to a stantard time format with hours.
                        songLength = time.strftime("%H:%M:%S",
                                                   time.gmtime(songSeconds))
                    elif songSeconds >= 60:  #Converts seconds to a stantard time format with no hours.
                        songLength = time.strftime("%M:%S",
                                                   time.gmtime(songSeconds))
                    else:  #Converts seconds to a stantard time format with hours.
                        songLength = time.strftime("%H:%M:%S",
                                                   time.gmtime(songSeconds))
                    print(queue)
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
                    isSongActive = True
                except:
                    await ctx.reply("Invalid link!", mention_author=False)
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
                print(url)
                queue.append(url)
                print("Queue: ", queue)
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
            isSongActive = False
        elif (ctx.author_voice is None):
            await ctx.reply(
                "You must be in a voice channel first so I can play it.",
                mention_author=False)
            print(f"Play command used, but bot was not in a voice channel.")
            isSongActive = False
        else:
            await ctx.reply("Bot is already playing", mention_author=False)
            print(f"Play command used, but bot was already playing music.")
            return

    # command to resume voice if it is paused

# ---------------------------------------- Play Skip Command ----------------------------------------
# Bot skips the current song and then plays audio from a YouTube link.

    @commands.command(aliases=['ps', 'playnow'])
    async def playskip(self, ctx, url):
        global voice
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)

        if voice.is_playing() and ctx.voice_client:
            voice.stop()
            await ctx.reply('Stopped', mention_author=False)
            isSongActive = False
            print(f"Stop command used, song is stopping...")
        elif not ctx.voice_client:
            await ctx.reply('You are not in a voice channel.',
                            mention_author=False)
            print(f"Stop command used, but author is not in a voice channel.")
        else:
            await ctx.reply('There is not song playing.', mention_author=False)
            print(f"Stop command used, but there is no song playing.")

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
            if not voice.is_playing(
            ) and ctx.voice_client:  #Makes sure bot isn't playing music and is in a voice channel.
                try:
                    await ctx.reply("Searching...", mention_author=False
                                    )  #Lets user know the command has started.
                    with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
                        info = ydl.extract_info(url, download=False)
                    uploaderSong = info['uploader']
                    uploaderIDSong = info['uploader_id']
                    requesterSong = ctx.message.author.id
                    isLooping = False  #Default is False.
                    isSongActive = False
                    isPaused = False  #Default is False.
                    URL = info['url']
                    songTitle = info['title']
                    songSeconds = info['duration']
                    songID = info['id']
                    songInfo = info
                    if songSeconds >= 3600:  #Converts seconds to a stantard time format with hours.
                        songLength = time.strftime("%H:%M:%S",
                                                   time.gmtime(songSeconds))
                    elif songSeconds >= 60:  #Converts seconds to a stantard time format with no hours.
                        songLength = time.strftime("%M:%S",
                                                   time.gmtime(songSeconds))
                    else:  #Converts seconds to a stantard time format with hours.
                        songLength = time.strftime("%H:%M:%S",
                                                   time.gmtime(songSeconds))
                    print(queue)
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
                    isSongActive = True
                except:
                    await ctx.reply("Invalid link!", mention_author=False)
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
                print(url)
                queue.append(url)
                print("Queue: ", queue)
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
            isSongActive = False
        elif (ctx.author_voice is None):
            await ctx.reply(
                "You must be in a voice channel first so I can play it.",
                mention_author=False)
            print(f"Play command used, but bot was not in a voice channel.")
            isSongActive = False
        else:
            await ctx.reply("Bot is already playing", mention_author=False)
            print(f"Play command used, but bot was already playing music.")
            return

    # command to resume voice if it is paused

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
        global isPaused
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if ctx.voice_client and ctx.author.voice:
            if voice.is_playing() and not isPaused:
                voice.pause()
                await ctx.reply('Song has been paused', mention_author=False)
                isPaused = True
                print(f"Pause command used, paused music.",
                      mention_author=False)
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
            isSongActive = False
            print(f"Stop command used, song is stopping...")
        elif not ctx.voice_client:
            await ctx.reply('You are not in a voice channel.',
                            mention_author=False)
            print(f"Stop command used, but author is not in a voice channel.")
        else:
            await ctx.reply('There is not song playing.', mention_author=False)
            print(f"Stop command used, but there is no song playing.")

# ---------------------------------------- Now Playing Command ----------------------------------------
# Shows information of the current song.

    @commands.command(aliases=['np', 'now', 'nowplaying', 'now playing'])
    async def now_playing(self, ctx):
        if ctx.voice_client:
            if songSeconds >= 3600:
                songLength = time.strftime("%H:%M:%S",
                                           time.gmtime(songSeconds))
            elif songSeconds >= 60:
                songLength = time.strftime("%M:%S", time.gmtime(songSeconds))
            else:
                songLength = time.strftime("%H:%M:%S",
                                           time.gmtime(songSeconds))
            songPlayingStatus = "Is Playing"
            if not isPaused:
                songPlayingStatus = "Is Playing"
            elif isPaused:
                songPlayingStatus = "Paused"
            else:
                songPlayingStatus = "Unknown (This is an error lol)"
            if voice.is_playing() or isPaused:
                if requesterSong is not None:
                    embed = discord.Embed(
                        title="Now Playing ♪... ",
                        description=
                        f"Title: [`{songTitle}`](https://www.youtube.com/watch?v={songID}) \nDuration: `{songLength}` \nUploaded by: [`{str(uploaderSong)}`](https://www.youtube.com/{uploaderIDSong}) \nRequested By: <@{requesterSong}> \n Status: `{songPlayingStatus}`",
                        color=0x44ff44)
                    embed.set_image(
                        url=f"https://img.youtube.com/vi/{songID}/0.jpg".
                        format(songID=songID))
                    await ctx.reply(embed=embed, mention_author=False)
                    print(
                        f"Now Playing command used, showing current song information..."
                    )
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
        if not ctx.voice_client:
            queue.clear()
            embed = discord.Embed(
                title="",
                description=
                f"There are no items in the queue! \n WARNING: The queue has no function right now, this is just a test.",
                color=0xff3c28)
            await ctx.reply(embed=embed, mention_author=False)
        if queue is not None:
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


async def setup(client):
    await client.add_cog(music(client))
