import discord
from discord.embeds import Embed
from discord.ext.commands import Cog
from discord.ext.commands import command


class Pfp(Cog):

	def __init__(self, bot):
		self.bot = bot

	@command(name="banner")
	async def getbanner(self, ctx, user: discord.User):
        url = f"cdn.discordapp.com/banners/{user.id}/"
		embed = Embed(title=f"{user.display_name}'s Banner")
		embed.set_image(url=user.avatar_url)
		await ctx.send(embed=embed)

	@Cog.listener()
	async def on_ready(self):
		if not self.bot.ready:
			self.bot.cogs_ready.ready_up("pfp")


def setup(bot):
	bot.add_cog(Pfp(bot))
