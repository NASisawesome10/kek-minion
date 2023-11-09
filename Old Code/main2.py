import discord
from discord.ext import commands
import yt_dlp
import os
import asyncio

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix='.', intents=discord.Intents.all())
discord.opus.load_opus("./libopus.so.0.8.0")


async def load():
	for filename in os.listdir('./cogs'):
		if filename.endswith('.py'):
			await client.load_extension(f'cogs.{filename[:-3]}')


async def main():
	await load()
	await client.start(
	    "MTA0MzczOTAzMDY1NjkyNTcxNg.G-J_Xs.sRrqI5EfeDfqypMFgZugRE1xFxdXtVpMUwAZ1w"
	)


asyncio.run(main())
