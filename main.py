import discord
import os
from discord.ext import commands
from settings import *

owner_ids = [118189214591483913]
# Intents are used to track member status and ownership
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", owner_ids=owner_ids, intents=intents)


# Add cogs from files
for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f"cogs.{filename[:-3]}")


bot.run(DISCORD_BOT_TOKEN)
