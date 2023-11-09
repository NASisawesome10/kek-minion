import discord
from discord.ext import commands
#import youtube_dl
import yt_dlp

import os

#https://replit.com/talk/learn/OPUS-SUPPORT-FOR-DISCORD-MUSIC-BOTS/37015?order=new
#use "kill 1" in Shell if discord blocks bot

# TO DOWNLOAD FFMPEG:
# ctrl+shift+s
# npm install ffmpeg-static
# node -e "console.log(require('ffmpeg-static'))"
# copy result to variable below:

FFMPEG_PATH = '/home/runner/test/node_modules/ffmpeg-static/ffmpeg'

# You must include this line for it to work

discord.opus.load_opus("./libopus.so.0.8.0")

#client = discord.Client()

client = commands.Bot(command_prefix='.', intents=discord.Intents.all())

client.remove_command('help')


@client.command(aliases=['h'])
async def help(ctx):
    embed = discord.Embed(
        title="Commands",
        description=
        f".help = Displays all available commands.\n.ping = Pings bot and sends its response time.\n.wise = Wise Mystical Tree\n.join = Joins voice channel user is currently in.\n.play = Plays a song only with a YouTube link.\n.leave = Leaves the voice channel the bot is in.\n.pause = Pauses the song currently playing.\n.resume = Resumes a song that is currently paused.\n.stop = Stops the song currently playing, cannot be resumed.\n\nIf the bot stops working or is bugging out, just ping @NASisawesome10 and let him know so that he can restart it or fix the bug.",
        color=0x44ff44)
    await ctx.send(embed=embed)


@client.command(aliases=['pi'])
async def ping(ctx):
    if round(client.latency * 1000) <= 50:
        embed = discord.Embed(
            title="PING",
            description=
            f"<:wisemysticaltree:1027671955064766514> The ping is **{round(client.latency *1000)}** milliseconds!",
            color=0x44ff44)
    elif round(client.latency * 1000) <= 100:
        embed = discord.Embed(
            title="PING",
            description=
            f"<:wisemysticaltree:1027671955064766514> \n The ping is **{round(client.latency *1000)}** milliseconds!",
            color=0xffd000)
    elif round(client.latency * 1000) <= 200:
        embed = discord.Embed(
            title="PING",
            description=
            f"<:wisemysticaltree:1027671955064766514> \n The ping is **{round(client.latency *1000)}** milliseconds!",
            color=0xff6600)
    else:
        embed = discord.Embed(
            title="PING",
            description=
            f"<:wisemysticaltree:1027671955064766514> \n The ping is **{round(client.latency *1000)}** milliseconds!",
            color=0x990000)
    await ctx.send(embed=embed)


@client.command(aliases=['w'])
async def wise(ctx):
    embed = discord.Embed(
        title="<:wisemysticaltree:1027671955064766514>",
        description=f"<:wisemysticaltree:1027671955064766514>")
    await ctx.send(embed=embed)


@client.command(aliases=['j'])
async def join(ctx):
    connected = ctx.author.voice
    #if connected:
    #await connected.channel.connect()

    #await ctx.send("Joined")
    #voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)

    if voice_client == None:
        await connected.channel.connect()
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        #voice.play(discord.FFmpegPCMAudio("Vine Boom Sound Effect.mp3"))
    else:
        await ctx.send(
            "The bot is already connected to a voice channel, dumbass.")


@client.command(aliases=['p', 'start'])
async def play(ctx, url):
    connected = ctx.author.voice
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send(
            "Wait for the current playing music to end or use the 'stop' command"
        )
        return
    if voice_client == None:
        await connected.channel.connect()
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        voice.stop()
    else:
        #await connected.channel.connect()
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        voice.stop()
    #voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='Jeneral')
    #await voiceChannel.connect()
    #voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

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
            os.rename(file, "song.mp3")
    #discord.opus.load_opus(discord.FFmpegPCMAudio("song.mp3"))
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        voice.stop()
        voice.play(discord.FFmpegPCMAudio("song.mp3"))
    #if voice_client == None:
    #await connected.channel.connect()
    #voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    #voice.play(discord.FFmpegPCMAudio("song.mp3"))
    #else:
    #voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    #voice.play(discord.FFmpegPCMAudio("song.mp3"))


@client.command(aliases=['l', 'dc', 'disconnect'])
async def leave(ctx):
    #voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    #if voice.is_connected():
    #await voice.disconnect()
    #await ctx.send("Leaving")
    #else:
    #await ctx.send("The bot is not connected to a voice channel.")
    #channel = ctx.message.author.voice.channel
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)

    if voice_client == None:
        await ctx.send("The bot is not connected to a voice channel, dumbass.")
    else:
        await voice.disconnect()


@client.command(aliases=['pa'])
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@client.command(aliases=['r'])
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@client.command(aliases=['st', 'halt'])
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()


@client.command(aliases=['big', 'shot'])
async def bigshot(ctx):
    connected = ctx.author.voice
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice_client == None:
        await connected.channel.connect()
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        voice.stop()
    else:
        voice.stop()
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        voice.play(
            discord.FFmpegPCMAudio("BIG SHOT [Super Smashing Fighters].wav"))


@client.command()
async def infolist(ctx):
    embed = discord.Embed(
        title="List of valid names",
        description=
        f"Cooper \n Jet \n Nick \n Adam \n Ian \n Ben \n Hunter \n Gage \n Jayden \n Andrew \n Omar \n \n Warning: Most of these names don't work yet because this command is still being worked on",
        color=0x44ff44)
    await ctx.send(embed=embed)


@client.command()
async def info(ctx, *, username=None):

    if username == 'Ben':
        embed = discord.Embed(
            title=username,
            description=
            f"**Discord** | <@244553215134138369> \n **YouTube** | [@RealBen0416](https://www.youtube.com/@user-mm8el9eg8j) \n **Steam** | [Ben0416](https://steamcommunity.com/id/Ben0416/) \n **Battle.net** | Tetris#11843 \n **Minecraft** | Ben0416 \n **Nintendo Friend Code** | SW-7839-5863-1482 \n ---------------------- \n **Schedule** \n __Tuesday__ \n # CS | <t:1677340800:t>-<t:1677345600:t> \n # English | <t:1677346200:t>-<t:1677351000:t> \n # Statistics | <t:1677351600:t>-<t:1677356400:t> \n __Wednesday__ \n # Physics Lecture | <t:1677346200:t>-<t:1677351000:t> \n # Physics Lab | <t:1677369600:t>-<t:1677376500:t> \n __Thursday__ \n # CS | <t:1677340800:t>-<t:1677345600:t> \n # English | <t:1677346200:t>-<t:1677351000:t> \n # Statistics | <t:1677351600:t>-<t:1677356400:t> \n # Physics Lecture | <t:1677357000:t>-<t:1677361800:t>",
            color=0x44ff44)
        embed.set_image(
            url=
            "https://cdn.discordapp.com/avatars/244553215134138369/887e0ea39250d6730e44e50fbddc3d66.webp?size=128"
        )
        await ctx.send(embed=embed)

    elif username == 'Nick':
        embed = discord.Embed(
            title=username,
            description=
            f"**Discord** | <@181442835420151808> \n **YouTube** | [@NASisawesome10](https://www.youtube.com/user/NASisawesome10) \n **Steam** | [NASisawesome10](https://steamcommunity.com/id/NASisawesome10/) \n **Battle.net** | NickelPickle#11689 \n **Minecraft** | NASisawesome10 \n ---------------------- \n **Schedule** \n __Wednesday__ \n # Work | <t:1677356100:t>-<t:1677376800:t> \n __Thursday__ \n # Work | <t:1677346200:t>-<t:1677376800:t> \n __Friday__ \n # Work | <t:1677346200:t>-<t:1677376800:t> \n __Saturday__ \n # Work | <t:1677331800:t>-<t:1677358800:t> \n __Sunday__ \n # Work | <t:1677331800:t>-<t:1677358800:t>",
            color=0x44ff44)
        embed.set_image(
            url=
            "https://cdn.discordapp.com/avatars/181442835420151808/009cc60b95edc13a1ec3c4c3b37e4779.webp?size=128"
        )
        await ctx.send(embed=embed)
    elif username == 'Ian':
        embed = discord.Embed(
            title=username,
            description=
            f"**Discord** | <@520542674726551562> \n **YouTube** | [@noice8911](https://www.youtube.com/channel/UC1a47K2AqJr-JV1OAEZxsGA) \n **Steam** | [Noice](https://steamcommunity.com/id/sansth3sk3l3ton/) \n **Minecraft** | Darkphaz0n \n **Nintendo Friend Code** | SW-2540-0616-1817 \n ---------------------- \n **Schedule** \n __Monday__ \n # Work | <t:1677362400:t>-<t:1677384000:t> \n __Wednesday__ \n # Work | <t:1677362400:t>-<t:1677384000:t> \n __Thursday__ \n # Work | <t:1677362400:t>-<t:1677384000:t> \n __Saturday__ \n # Work | <t:1677362400:t>-<t:1677387600:t> \n __Sunday__ \n # Work | <t:1677362400:t>-<t:1677384000:t>",
            color=0x44ff44)
        embed.set_image(
            url=
            "https://cdn.discordapp.com/avatars/520542674726551562/825124336759192af5f99a5d0f171bca.webp?size=128"
        )
        await ctx.send(embed=embed)
    elif username == 'Adam':
        embed = discord.Embed(
            title=username,
            description=
            f"**Discord** | <@294477835626610698> \n **Steam** | [Hunter of Thugs](https://steamcommunity.com/id/do_you_ever_just/) \n **Minecraft** | BusterofNuts \n **Nintendo Friend Code** | SW-2151-0277-8918",
            color=0x44ff44)
        embed.set_image(
            url=
            "https://cdn.discordapp.com/avatars/294477835626610698/34cd9acb790b26d5b07833976c52c013.webp?size=128"
        )
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title="Invalid Name!",
            description=
            f"Please enter a valid name! Type `.infolist` to show the valid names.",
            color=0x44ff44)
        await ctx.send(embed=embed)
        return


#{ctx.author.mention}
client.run(
    "MTA0MzczOTAzMDY1NjkyNTcxNg.G-J_Xs.sRrqI5EfeDfqypMFgZugRE1xFxdXtVpMUwAZ1w")
# good luck!
