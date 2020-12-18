import discord
from discord.ext import commands
import random
from datetime import datetime

class Christmas(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name = 'advent', pass_context=True, help = 'Get a random item from the advent calander.')
    @commands.cooldown(1,86400, commands.BucketType.user)
    async def advent(self, ctx):
        items = ["Chocolate Reindeer", "Chocolate Snowflake", "Chocolate Elf", "Chocolate Santa", "Chocolate Christmas Tree"]
        today = datetime.today()
        await ctx.send(f":e_mail: {ctx.message.author.mention} Check your DMs!")
        if today.month == 12 and today.day <= 25:
            days = 25 - int(today.day)
            await ctx.message.author.send("There is " + str(days) + " day(s) left until christmas!")
            await ctx.message.author.send("You got a " + str(random.choice(items)))

        else:
            await ctx.message.author.send("It is not december yet - or is past christmas!")

def setup(bot):
    bot.add_cog(Christmas(bot))