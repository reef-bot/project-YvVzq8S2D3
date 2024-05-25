# main.py

import discord
from discord.ext import commands
from config.config import PREFIX
from modules.rules import Rules
from modules.profanity_filter import ProfanityFilter
from modules.report_feature import ReportFeature
from modules.reputation_system import ReputationSystem
from modules.logging_system import LoggingSystem
from utils.helper_functions import get_server_prefix

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.guild is None:
        return

    server_prefix = get_server_prefix(message.guild.id)
    if not message.content.startswith(server_prefix):
        return

    await bot.process_commands(message)

bot.add_cog(Rules(bot))
bot.add_cog(ProfanityFilter(bot))
bot.add_cog(ReportFeature(bot))
bot.add_cog(ReputationSystem(bot))
bot.add_cog(LoggingSystem(bot))

bot.run("YOUR_DISCORD_TOKEN")