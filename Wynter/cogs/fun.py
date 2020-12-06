import http.client
import mimetypes
import json
import discord
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(name = 'hug', pass_context=True, help = 'Hug a user')
    @commands.guild_only()
    async def info(self, ctx, *hugged):
        conn = http.client.HTTPSConnection("api.furrycentr.al")
        payload = ''
        headers = {
        'Cookie': '__cfduid=d9a224e3d8c1cb5402581c2ae57ae3ec21605192790'
        }
        conn.request("GET", "/sfw/hug/", payload, headers)
        res = conn.getresponse()
        data = res.read()
        data = data.decode("utf-8")
        data = json.loads(data)
        htxt = ""
        for str in hugged:
            htxt = htxt + str + ", "
        embed = discord.Embed(title = "Hug!", description = f"{ctx.message.author.mention} pulls {htxt} into a giant hug!", color=0x00ff00)
        embed.set_image(url = data["result"]["imgUrl"])
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Fun(bot))

