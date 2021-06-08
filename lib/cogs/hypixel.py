from discord.ext.commands import Cog
from discord.ext.commands import command
from aiohttp import request
import requests
from discord import Embed


class Hypixel(Cog):
	def __init__(self, bot):
		self.bot = bot

	@command(name="online")
	async def check_online(self, ctx):
		uuid = requests.get("https://api.mojang.com/users/profiles/minecraft/Diablo_TDL").json()['id']
		params = {
			"key": "96288366-63f2-458f-98ab-dcafc0e527cf",
			"uuid": uuid
		}
		URL = "https://api.hypixel.net/status"
		async with request('GET', URL, params=params) as resposne:
			data = await resposne.json()
			embed = Embed(title="Status",description='Online' if data["session"]["online"] else 'Offline', color=0xFF5733)
			await ctx.send(embed=embed)
				
	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("hypixel")


def setup(bot):
	bot.add_cog(Hypixel(bot))