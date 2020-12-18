import discord
from discord.ext import commands
import http.client
import mimetypes
import json

class NSFW(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name = 'gay', pass_context=True, help = 'Get a gay yiff image')
    @commands.guild_only()
    @commands.is_nsfw()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def gay(self, ctx):
        conn = http.client.HTTPSConnection("api.furrycentr.al")
        payload = ''
        headers = {
        'Cookie': '__cfduid=d9a224e3d8c1cb5402581c2ae57ae3ec21605192790'
        }
        conn.request("GET", "/nsfw/yiff/gay/", payload, headers)
        res = conn.getresponse()
        data = res.read()
        data = data.decode("utf-8")
        data = json.loads(data)
        embed = discord.Embed(title = "Oh murr!", description = "I hope you enjoy this image ;)", color=0x00ff00)
        embed.set_image(url = data["result"]["imgUrl"])
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(NSFW(bot))