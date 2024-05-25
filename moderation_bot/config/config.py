# config.py

import discord
from discord.ext import commands
import logging

class Config:
    def __init__(self, bot):
        self.bot = bot
        self.prefix = "!"
        self.rules_channel_id = 1234567890
        self.profane_words = ["bad_word1", "bad_word2"]
        self.report_channel_id = 1234567891
        self.reputation_threshold = 3

    async def get_prefix(self, bot, message):
        return self.prefix

    async def get_rules_channel(self):
        return self.bot.get_channel(self.rules_channel_id)

    async def get_profane_words(self):
        return self.profane_words

    async def get_report_channel(self):
        return self.bot.get_channel(self.report_channel_id)

    async def get_reputation_threshold(self):
        return self.reputation_threshold

    async def setup(self):
        await self.bot.change_presence(activity=discord.Game(name="Moderating the server"))
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# End of config.py