import os
import discord
import aiohttp
from discord.ext import commands, tasks
from dotenv import load_dotenv, dotenv_values 

load_dotenv() #loads the .env file keys

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix = "-", intents = discord.Intents.all(), application_id = os.getenv("APPLICATION_ID") ) #sets the prefix, intents, and application id
        self.initial_extensions = [ #list of cogs to load
         "cogs.steamSearch",
        ]
    
    async def setup_hook(self):
        self.session = aiohttp.ClientSession()
        for ext in self.initial_extensions: #loads the cogs
            await self.load_extension(ext)
        await bot.tree.sync() #syncs the slash commands with discord

    async def close(self):
        await super().close()
        await self.session.close()

    
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!') #prints when the bot is ready
    

bot = MyBot()
bot.run(os.getenv("TOKEN"))