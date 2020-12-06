import discord
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(name = 'info', pass_context=True, help = 'Shows bot info')
    async def info(self, ctx):
        embed = discord.Embed(title = "Bot Information", description = "Libraries used:\nPython v3.9.0 \nDiscord.py v1.5.1 \nPyMySQL v0.10.1 \n\nAdditional Credits:\nNanofaux#0621 - for helping aide me into Python.", color=0x00ff00)
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(embed = embed)
    
    @commands.command(name = 'ping', pass_context=True, help= 'Shows the bot latency connecting to discord.')
    async def ping(self,ctx):
        ping = self.bot.latency * 1000
        embed = discord.Embed(title = "Pong!", description = '___Took {0}'.format(round(ping, 1)) + "ms___" , color=0x00ff00)
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(embed = embed)

    @commands.command(name = 'invite', pass_context=True, help= 'Shows the bot\'s invite.')
    async def invite(self,ctx):
        embed = discord.Embed(title = "Here ya go!", description = "My invite is https://furrycentr.al/add" , color=0x00ff00)
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(embed = embed)

    @commands.command(name = 'serverinfo', pass_context= True, help='Shows information about the current guild')
    @commands.guild_only()
    async def serverinfo(self,ctx):
        embed = discord.Embed(title=ctx.message.guild.name, color=0x00ff00)
        embed.add_field(name="Owner", value=ctx.message.guild.owner, inline=False)
        embed.add_field(name="Date of creation", value=ctx.message.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
        embed.add_field(name="Region", value=ctx.message.guild.region, inline=False)
        embed.set_thumbnail(url = ctx.message.guild.icon_url)
        return await ctx.message.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Info(bot))