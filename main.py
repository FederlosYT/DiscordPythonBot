import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix="your prefix")

@client.event
async def on_ready():
	print("Bot is ready!")



client.run('Your_Token_Here')