import discord
from discord.ext import commands
import aiohttp
import asyncio
import json
import os
from dotenv import load_dotenv

load_dotenv()
imgusr = os.getenv('IMGUSR')
imgpw = os.getenv('IMGPW')

class Meme(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name = 'changemymind', pass_context=True, help = 'Generates a change my mind meme using imgur')
    @commands.cooldown(1,5, commands.BucketType.user)
    async def changemymind(self, ctx, *, text):
        params = {'text0': text, 'username': imgusr, 'password': imgpw, 'template_id': '129242436'}
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.imgflip.com/caption_image", params = params) as resp:
                data = await resp.text()
                data = json.loads(data)
                url = data["data"]["url"]
                return await ctx.send(url)

def setup(bot):
    bot.add_cog(Meme(bot))