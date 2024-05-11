import os
import discord
import aiohttp
from discord.ext import commands, tasks
from dotenv import load_dotenv, dotenv_values 

load_dotenv() 


GUILD_ID = os.getenv("GUILD_ID")
if GUILD_ID is None:
    print("YAY")


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix = "-", intents = discord.Intents.all(), application_id = os.getenv("APPLICATION_ID") )
        self.initial_extensions = [
         "cogs.steamSearch",
        ]
    
    async def setup_hook(self):
        self.session = aiohttp.ClientSession()
        for ext in self.initial_extensions:
            await self.load_extension(ext)
        
        GUILD_ID = os.getenv("GUILD_ID")
        if GUILD_ID is None:
            print("SUCESS")

        await bot.tree.sync(guild=discord.Object(id = GUILD_ID))

    async def close(self):
        await super().close()
        await self.session.close()

    
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
    

#bot = MyBot()
#bot.run(os.getenv("TOKEN"))