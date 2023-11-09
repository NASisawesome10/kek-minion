import discord
from discord.ext import commands
#import youtube_dl
import yt_dlp

import os

from music_cog import music_cog

#https://replit.com/talk/learn/OPUS-SUPPORT-FOR-DISCORD-MUSIC-BOTS/37015?order=new
#use "kill 1" in Shell if discord blocks bot

# TO DOWNLOAD FFMPEG:
# ctrl+shift+s
# npm install ffmpeg-static
# node -e "console.log(require('ffmpeg-static'))"
# copy result to variable below:
# built-in checks for commands: https://gist.github.com/Painezor/eb2519022cd2c907b56624105f94b190

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
        f"**General Commands** \n `.help` = Displays all available commands. \n `.ping` = Pings bot and sends its response time. \n `.wise` = Wise Mystical Tree \n `.info` = Displays info about someone when a valid name is entered. If an invalid name or nothing is entered, it will show a list of valid names. \n `.ip` = Gives the IP address for the Minecraft server. \n \n **Music Commands** \n `.join` = Joins voice channel user is currently in. \n `.play` = Plays a song only with a YouTube link. \n `.leave` = Leaves the voice channel the bot is in. \n `.pause` = Pauses the song currently playing. \n `.resume` = Resumes a song that is currently paused. \n `.stop` = Stops the song currently playing, cannot be resumed. \n \n If the bot stops working or is bugging out, just ping <@181442835420151808> and let him know so that he can restart it or fix the bug.",
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
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        embed = discord.Embed(
            title="You are not in a voice channel!",
            description=f"You must be in a voice channel to have the bot join.",
            color=0xff3c28)
        await ctx.send(embed=embed)


@client.command(aliases=['p'])
async def play(ctx, url):
    song_there = os.path.isfile(
        "song.mp3")  #Defines variable as the existence of the file 'song.mp3'
    try:
        if song_there:  #If there is a file named 'song.mp3...'
            os.remove("song.mp3")  #...Delete it
    except PermissionError:
        await ctx.send(
            "Wait for the current playing music to end or use the 'stop' command"
        )
        return
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        #voice.stop()
    else:
        embed = discord.Embed(
            title="You are not in a voice channel!",
            description=f"You must be in a voice channel to have the bot join.",
            color=0xff3c28)
        await ctx.send(embed=embed)
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        #voice.stop()

    ydl_opts = { #Parameters for the audio download
        'format':
        'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(
            [url]
        )  #Downloads audio from video with the previously mentioned parameters
    for file in os.listdir("./"):
        if file.endswith(".mp3"):  #Finds newly downloaded file.
            await os.rename(file, "song.mp3"
                            )  #Renames the new audio file to 'song.mp3'
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        #voice.stop()
        voice.play(discord.FFmpegPCMAudio("song.mp3"))  #Plays audio


@client.command(aliases=['l', 'dc', 'disconnect'])
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice_client = discord.utils.get(client.voice_clients, guild=ctx.guild)

    if voice_client == None:
        embed = discord.Embed(
            title="The bot is not connected to a voice channel.",
            description=f"dumbass",
            color=0xff3c28)
        await ctx.send(embed=embed)
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


names = ["ben", "nick", "ian", "adam", "jayden", "gage", "mikal", "omar"]
usernames = [
    "realben0416", "ben0416", "nasisawesome10", "polaris", "Ædam", "bluejay",
    "mazi", "zaideth", "ot"
]


@client.command()
@commands.has_any_role(765010827899437129, 702328225971568661,
                       723728937171288099)
async def info(ctx, *, username=None):
    if username == None:  #Nothing
        embed = discord.Embed(
            title="Invalid Name!",
            description=
            f"Please enter a valid name from below: \n \n # **Nick** \n # **Adam** \n # **Ian** \n # **Ben** \n # **Jayden** \n # **Gage** \n \n Note: More names will be added and if you want to be added feel free to ping <@181442835420151808>.",
            color=0xff3c28)
        await ctx.send(embed=embed)
    if username.lower() == names[0] or username.lower(
    ) == usernames[0] or username.lower() == usernames[1]:  #Ben
        embed = discord.Embed(
            title="Ben",
            description=
            f"**Socials** \n # Discord | <@244553215134138369> \n # YouTube | [`RealBen0416`](https://www.youtube.com/@user-mm8el9eg8j) \n # Twitch | [`RealBen0416`](https://www.twitch.tv/realben0416) \n # Twitter | [`@RealBen0416`](https://twitter.com/RealBen0416) \n \n **Games** \n # Steam | [`Ben0416`](https://steamcommunity.com/id/Ben0416/) \n # Battle.net | `Tetris#11843` \n # Minecraft | `Ben0416` \n # Nintendo Friend Code | `SW-7839-5863-1482` \n ---------------------- \n **Schedule** \n __Tuesday__ \n # CS | <t:1677340800:t>-<t:1677345600:t> \n # English | <t:1677346200:t>-<t:1677351000:t> \n # Statistics | <t:1677351600:t>-<t:1677356400:t> \n __Wednesday__ \n # Physics Lecture | <t:1677346200:t>-<t:1677351000:t> \n # Physics Lab | <t:1677369600:t>-<t:1677376500:t> \n __Thursday__ \n # CS | <t:1677340800:t>-<t:1677345600:t> \n # English | <t:1677346200:t>-<t:1677351000:t> \n # Statistics | <t:1677351600:t>-<t:1677356400:t> \n # Physics Lecture | <t:1677357000:t>-<t:1677361800:t>",
            color=0x44ff44)
        embed.set_image(
            url=
            "https://cdn.discordapp.com/avatars/244553215134138369/887e0ea39250d6730e44e50fbddc3d66.webp?size=128"
        )
        await ctx.send(embed=embed)

    elif username.lower() == names[1] or username.lower(
    ) == usernames[2]:  #Nick
        embed = discord.Embed(
            title="Nick",
            description=
            f"**Socials** \n # Discord | <@181442835420151808> \n # YouTube | [`NASisawesome10`](https://www.youtube.com/user/NASisawesome10) \n \n **Games** \n # Steam | [`NASisawesome10`](https://steamcommunity.com/id/NASisawesome10/) \n # Battle.net | `NickelPickle#11689` \n # Minecraft | `NASisawesome10` \n ---------------------- \n **Schedule** \n __Wednesday__ \n # Work | <t:1677356100:t>-<t:1677376800:t> \n __Thursday__ \n # Work | <t:1677346200:t>-<t:1677376800:t> \n __Friday__ \n # Work | <t:1677346200:t>-<t:1677376800:t> \n __Saturday__ \n # Work | <t:1677331800:t>-<t:1677358800:t> \n __Sunday__ \n # Work | <t:1677331800:t>-<t:1677358800:t>",
            color=0x44ff44)
        embed.set_image(
            url=
            "https://cdn.discordapp.com/avatars/181442835420151808/009cc60b95edc13a1ec3c4c3b37e4779.webp?size=128"
        )
        await ctx.send(embed=embed)
    elif username.lower() == names[2] or username.lower(
    ) == usernames[3]:  #Ian
        embed = discord.Embed(
            title="Ian",
            description=
            f"**Socials** \n # Discord | <@520542674726551562> \n # YouTube | [`ポラリス`](https://www.youtube.com/@noice8911) \n \n **Games** \n # Steam | [`Noice`](https://steamcommunity.com/id/sansth3sk3l3ton/) \n # Minecraft | `Darkphaz0n` \n # Nintendo Friend Code | `SW-2540-0616-1817` \n ---------------------- \n **Schedule** \n __Monday__ \n # Work | <t:1677362400:t>-<t:1677384000:t> \n __Wednesday__ \n # Work | <t:1677362400:t>-<t:1677384000:t> \n __Thursday__ \n # Work | <t:1677362400:t>-<t:1677384000:t> \n __Saturday__ \n # Work | <t:1677362400:t>-<t:1677387600:t> \n __Sunday__ \n # Work | <t:1677362400:t>-<t:1677384000:t>",
            color=0x44ff44)
        embed.set_image(
            url=
            "https://cdn.discordapp.com/avatars/520542674726551562/825124336759192af5f99a5d0f171bca.webp?size=128"
        )
        await ctx.send(embed=embed)
    elif username.lower() == names[3] or username.lower(
    ) == usernames[4]:  #Adam
        embed = discord.Embed(
            title="Adam",
            description=
            f"**Socials** \n # Discord | <@294477835626610698> \n \n **Games**\n # Steam | [`Hunter of Thugs`](https://steamcommunity.com/id/do_you_ever_just/) \n # Minecraft | `BusterofNuts` \n # Nintendo Friend Code | `SW-2151-0277-8918`",
            color=0x44ff44)
        embed.set_image(
            url=
            "https://cdn.discordapp.com/avatars/294477835626610698/34cd9acb790b26d5b07833976c52c013.webp?size=128"
        )
        await ctx.send(embed=embed)
    elif username.lower() == names[4] or username.lower(
    ) == usernames[5]:  #Jayden
        embed = discord.Embed(
            title="Jayden",
            description=
            f"**Socials** \n # Discord | <@378294978490925056> \n # YouTube | [`TheOfficialBlueJay`](https://www.youtube.com/@TheOfficialBlueJay) \n # Twitch | [`TheOfficialBlueJay]`(https://www.twitch.tv/theofficialbluejay) \n \n **Games** \n # Steam | [`Jayhalkio826`](https://steamcommunity.com/profiles/76561198159506442/) \n # Playstation Network | `Official-BlueJay` \n # Battle.net | `BlueJay22#1686` \n # Minecraft | `BlueJay826`",
            color=0x44ff44)
        embed.set_image(
            url=
            "https://cdn.discordapp.com/avatars/378294978490925056/0313e47c1bd4df9cd15bc9cc967d9d8f.webp?size=128"
        )
        await ctx.send(embed=embed)
    elif username.lower() == names[5] or username.lower(
    ) == usernames[6]:  #Gage
        embed = discord.Embed(
            title="Gage",
            description=
            f"**Socials** \n # Discord | <@209781510453067776> \n # YouTube | [`Mazi`](https://www.youtube.com/@mazi48) \n \n **Games** \n # Steam | [`Mazi`](https://steamcommunity.com/id/mazikif/) \n # Battle.net |  `Lulzboat#1392` \n # Minecraft | `mazikif`",
            color=0x44ff44)
        embed.set_image(
            url=
            "https://cdn.discordapp.com/avatars/209781510453067776/351b0578c12494ca95c32f5117073c8b.webp?size=128"
        )
        await ctx.send(embed=embed)
    elif username.lower() == names[6] or username.lower(
    ) == usernames[7]:  #Mikal
        embed = discord.Embed(
            title="Mikal",
            description=
            f"**Socials** \n # Discord | <@931000601263878174> \n # Discord (Alt) | <@259808943138668545> \n # YouTube | [`Zaideth`](https://www.youtube.com/@zaideth4717) \n # Twitch | [`GGZaideth`](https://www.twitch.tv/ggzaideth) \n \n **Games** \n # Steam | [`ggzaideth`](https://steamcommunity.com/profiles/76561199245355998) \n # Minecraft | `_zaideth_` \n ---------------------- \n **Schedule** \n __Wednesday__ \n # Work | <t:1677589200:t>-<t:1677625200:t> \n __Thursday__ \n # Work | <t:1677589200:t>-<t:1677625200:t> \n __Friday__ \n # Work | <t:1677589200:t>-<t:1677625200:t> \n __Saturday__ \n # Work | <t:1677589200:t>-<t:1677625200:t>",
            color=0x44ff44)
        embed.set_image(
            url=
            "https://cdn.discordapp.com/avatars/931000601263878174/e89d82aa9cc4c147c17b800bbecb5a8c.webp?size=128"
        )
        await ctx.send(embed=embed)
    elif username.lower() == names[7] or username.lower(
    ) == usernames[8]:  #Omar
        embed = discord.Embed(
            title="Omar",
            description=
            f"**Socials** \n # Discord | <@245681120040058890> \n # Twitch | [`OT2003`](https://www.twitch.tv/ot2003) \n \n **Games** \n # Steam | [`Omies`](https://steamcommunity.com/profiles/76561198198643482) \n # Xbox | `OT2003` \n # Epic | `Omies Ha` \n # Battle.net | `Omies#11918` \n # Minecraft | `Omies_Ha` \n # Nintendo Friend Code | `SW-7113-1712-5337`",
            color=0x44ff44)
        embed.set_image(
            url=
            "https://cdn.discordapp.com/avatars/245681120040058890/7c5800d7e834ff98c654e62a4165c7f6.webp?size=128"
        )
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title="Invalid Name!",
            description=
            f"Please enter a valid name from below: \n \n # **Nick** \n # **Adam** \n # **Ian** \n # **Ben** \n # **Jayden** \n # **Gage** \n \n Note: More names will be added and if you want to be added feel free to ping <@181442835420151808>.",
            color=0xff3c28)
        await ctx.send(embed=embed)


ips = ["kek", "kexxit"]


@client.command(aliases=['minecraft', 'address'])
async def ip(ctx, server=None):
    if server == None:
        embed = discord.Embed(
            title="Invalid Server!",
            description=
            f"Please enter a valid server from below: \n \n # **KeK** \n # **Kexxit**",
            color=0xff3c28)
        await ctx.send(embed=embed)
    elif server.lower() == ips[0]:
        embed = discord.Embed(title="KeK Incorporated Minecraft IP",
                              description=f"`KeK_Incorporated.aternos.me`",
                              color=0x44ff44)
        await ctx.send(embed=embed)
    elif server.lower() == ips[1]:
        embed = discord.Embed(title="Kexxit Minecraft IP",
                              description=f"`142.44.135.69:25582`",
                              color=0x44ff44)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title="Invalid Server!",
            description=
            f"Please enter a valid server from below: \n \n # **KeK** \n # **Kexxit**",
            color=0xff3c28)
        await ctx.send(embed=embed)


client.run(
    "MTA0MzczOTAzMDY1NjkyNTcxNg.G-J_Xs.sRrqI5EfeDfqypMFgZugRE1xFxdXtVpMUwAZ1w")
# good luck!
