import discord
from discord.ext import commands
import music 

cogs = [music]

client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)


client.run("OTIxNzQyOTk1MDA1NTA1NjA3.Yb3WDw.cHFqFNH8LKPMi1L8vXQTpXZH5m0")