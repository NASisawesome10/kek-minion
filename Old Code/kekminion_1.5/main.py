import keep_alive

import discord
from discord.ext import commands
#import yt_dlp
import os
import asyncio
#import aiohttp
#import openai
#import traceback
#import datetime

#pip install openai
#python3 -m pip install -U yt-dlp
# ^^^ run when starting bot for the first time. ^^^
#https://stackoverflow.com/questions/71873182/no-module-named-openai
#https://platform.openai.com/account/api-keys

#https://uptimerobot.com/dashboard#mainDashboard

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix='.', intents=discord.Intents.all())
discord.opus.load_opus("./libopus.so.0.8.0")
FFMPEG_PATH = '/home/runner/test/node_modules/ffmpeg-static/ffmpeg'

#openai.api_key = "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"

client.remove_command('help')


async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')
            print(f"{filename} Loaded")


async def main():
    await load()
    await client.start(os.environ['TOKEN'])


@client.event
async def on_ready():
    print("Bot is Online!")
    try:
        synced = await client.tree.sync()
        print(f"Syned {len(synced)} command(s)")
    except Exception as e:
        print(e)


# # ---------------------------------------- ChatGPT Command ----------------------------------------
# # Uses ChatGPT AI to generate a message from the author.
# @client.command(aliases=['gpt', 'ai'])
# async def chatgpt(ctx, query):
#     print(query)
#     await ctx.reply("Generating ChatGPT message...", mention_author=False)
#     response = openai.Completion.create(model="text-davinci-003",
#                                         prompt=query,
#                                         temperature=0.3,
#                                         max_tokens=4000,
#                                         top_p=1,
#                                         frequency_penalty=1,
#                                         presence_penalty=1,
#                                         stop=[" Human:", " AI:"])
#     text = response['choices'][0]['text']
#     embed = discord.Embed(title="Here is your answer", description=text)
#     print(text)
#     await ctx.reply(embed=embed)

#async def chatgpt(ctx, *args):
#    input = [*args]
#    await ctx.reply("Generating ChatGPT message...", mention_author=False)
#    print("ChatGPT command used, generating message...")
#    response = openai.Completion.create(model="text-davinci-003",
#                                        prompt=input,
#                                        temperature=0.5,
#                                        max_tokens=200,
#                                        top_p=1,
#                                        frequency_penalty=1,
#                                        presence_penalty=1,
#                                        stop=[" Human:", " AI:"])
#    text = response['choices'][0]['text']
#    print("ChatGPT prompt: [", *args, "]")
#    print("--------------------" + text + "\n--------------------")
#    await ctx.reply(" " + text, mention_author=False)

# ---------------------------------------- Help Command ----------------------------------------
# Shows a list of all available commands.


@client.command(aliases=['h'])
async def help(ctx):
    embed = discord.Embed(
        title="Commands",
        description=
        f"**General Commands** \n `.help` = Displays all available commands. \n `.ping` = Pings bot and sends its response time. \n `.info` = Displays info about someone when a valid name is entered. If an invalid name or nothing is entered, it will show a list of valid names. \n `.ip` = Gives the IP address for a Minecraft server. If an invalid name or nothing is entered, it will show a list of valid server ips. \n \n **Music Commands** \n `.join` = Joins voice channel user is currently in. \n `.play` = Plays a song only with a YouTube link. \n `.leave` = Leaves the voice channel the bot is in. \n `.pause` = Pauses the song currently playing. \n `.resume` = Resumes a song that is currently paused. \n `.stop` = Stops the song currently playing, cannot be resumed. \n \n If the bot stops working or is bugging out, just ping <@181442835420151808> and let him know so that he can restart it or fix the bug.",
        color=0x44ff44)
    await ctx.reply(embed=embed, mention_author=False)
    print(f"Help command used. Displaying a list of available commands...")


# ---------------------------------------- Ping Command ----------------------------------------
# Shows the response time of the Bot.


@client.command(aliases=['pi'])
async def ping(ctx):
    if round(client.latency * 1000) <= 50:
        embed = discord.Embed(
            title="PING",
            description=
            f"<:winton:1041562433510195251> The ping is **{round(client.latency *1000)}** milliseconds!",
            color=0x44ff44)
    elif round(client.latency * 1000) <= 100:
        embed = discord.Embed(
            title="PING",
            description=
            f"<:winton:1041562433510195251> \n The ping is **{round(client.latency *1000)}** milliseconds!",
            color=0xffd000)
    elif round(client.latency * 1000) <= 200:
        embed = discord.Embed(
            title="PING",
            description=
            f"<:winton:1041562433510195251> \n The ping is **{round(client.latency *1000)}** milliseconds!",
            color=0xff6600)
    else:
        embed = discord.Embed(
            title="PING",
            description=
            f"<:winton:1041562433510195251> \n The ping is **{round(client.latency *1000)}** milliseconds!",
            color=0x990000)
    await ctx.reply(embed=embed, mention_author=False)
    print(
        f"Ping command used. Ping time is {round(client.latency *1000)} milliseconds."
    )


keep_alive.keep_alive()
asyncio.run(main())
