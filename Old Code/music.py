import discord
from discord.ext import commands
import os
import yt_dlp


class music(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def test(self, ctx):
		await ctx.send("Test")

	@commands.Cog.listener()
	async def on_ready(self):
		print("On")

	@commands.command(aliases=['j'])
	async def join(self, ctx):
		if (ctx.author.voice):
			channel = ctx.message.author.voice.channel
			await channel.connect()
		else:
			embed = discord.Embed(
			    title="You are not in a voice channel!",
			    description=
			    f"You must be in a voice channel to have the bot join.",
			    color=0xff3c28)
			await ctx.send(embed=embed)

	@commands.command(aliases=['l', 'dc', 'disconnect'])
	async def leave(self, ctx):
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


names = ["ben", "nick", "ian", "adam", "jayden", "gage", "mikal", "omar"]
usernames = [
    "realben0416", "ben0416", "nasisawesome10", "polaris", "Ædam", "bluejay",
    "mazi", "zaideth", "ot"
]


async def setup(client):
	await client.add_cog(music(client))
