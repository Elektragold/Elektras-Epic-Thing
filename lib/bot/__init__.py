from discord.ext.commands import Bot as BotBase, CommandNotFound, Context
from discord import Intents, Embed

from glob import glob
from asyncio import sleep

PREFIX = "$"
OWNER_IDS = [315447222567305216]
COGS = [path.split("\\")[-1][:-3] for path in glob("./lib/cogs/*.py")]


class Ready(object):
    def __init__(self):
        for cog in COGS:
            setattr(self, cog, False)

    def ready_up(self, cog):
        setattr(self, cog, True)
        print(f"{cog} ready")

    def all_ready(self):
        return all([getattr(self, cog) for cog in COGS])


class Bot(BotBase):
    def __init__(self):

        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.cogs_ready = Ready()

        super().__init__( 
            command_prefix=PREFIX, 
            owner_ids=OWNER_IDS, 
            intents=Intents.all()
        )

    def setup(self):
        for cog in COGS:
            self.load_extension("lib.cogs."+cog)
            print(f"{cog} loaded")

        print("setup complete")

    def run(self, version):
        self.VERSION = version

        print("running setup")
        self.setup()

        with open("./lib/bot/token.0", 'r', encoding="utf-8") as tf:
            self.TOKEN = tf.read()
        print("running bot")
        super().run(self.TOKEN, reconnect=True)

    # async def process_commands(self, message):
    #     ctx = await self.get_context(message, cls=Context)
        
    #     if ctx.command is not None and ctx.guild is not None:
    #         if not self.ready:
    #             await self.invoke(ctx)
    #     else:
    #         await ctx.send("I'm not ready to recieve commands, wait for a few seconds")

    async def on_connect(self):
        print("Bot connected")
    
    async def on_disconnect(self):
        print("bot disconnected")

    async def on_error(self, err, *args, **kwargs):
        if err == "on_command_error":
            await args[0].send("Something went wrong")
        
        await self.stdout.send("An error occurred")

        raise

    async def on_command_error(self, ctx, exc):
        if isinstance(exc, CommandNotFound):
            pass
        elif hasattr(exc, "original"):
            raise exc
        else:
            raise exc

    async def on_ready(self):
        if not self.ready:
            self.stdout = self.get_channel(848155636549156867)
            self.guild = self.get_guild(848155636549156864)

            await self.stdout.send("online")

            while not self.cogs_ready.all_ready():
                await sleep(0.5)

            self.ready = True
            print("bot ready")

        else:
            print("bot reconnected")

    async def on_message(self, message):
        if not message.author.bot:
            await self.process_commands(message)


bot = Bot()