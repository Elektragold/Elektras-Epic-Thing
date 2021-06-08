from discord.embeds import Embed
from discord.ext.commands import Cog
from discord.ext.commands import command
import discord
import requests


class Pfp(Cog):

	def __init__(self, bot):
		self.bot = bot

	@command(name="getpfp")
	async def getpfp(self, ctx, user:discord.User):
		# headers = {"Authorization": f"Bot {self.bot.TOKEN}"}
		# avatar_id = requests.get(f"https://discord.com/api/users/{user.id}", headers=headers).json()["avatar"]
		embed = Embed(title=f"{user.display_name}'s Avatar")
		embed.set_image(url=user.avatar_url)
		# embed.set_image(url=f"https://cdn.discordapp.com/avatars/{user.id}/{avatar_id}.png")
		await ctx.send(embed=embed)


	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("pfp")


def setup(bot):
	bot.add_cog(Pfp(bot))