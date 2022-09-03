from discord.ext import commands
import discord

from aiomysql import create_pool


class Shikimori(commands.Bot):
    def __init__(self, **kwargs):
        intents = discord.Intents.all()
        intents.typing = False
        kwargs["intents"] = intents
        kwargs["command_prefix"] = "s!"
        self.mysql = kwargs["mysql"]
        super().__init__(**kwargs)

    async def setup_hook(self) -> None:
        self.pool = await create_pool(**self.mysql)
        for name in ["twitter"]:
            await self.load_extension("cogs.{}".format(name))
