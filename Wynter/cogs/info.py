import discord
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(name = 'info', pass_context=True, help = 'Shows bot info')
    @commands.cooldown(1,5, commands.BucketType.user)
    async def info(self, ctx):
        embed = discord.Embed(title = "Bot Information", description = "Libraries used:\nPython v3.9.0 \nDiscord.py v1.6.0a \nPyMySQL v0.10.1 \n\nAdditional Credits:\nNanofaux#0621 - for helping aide me into Python. \nMurdecoi#3541 - for aiding with moderation command testing. \nSkipper:tm:#6968 - for their suggestion of the RP scenario generator. \nAll the beta testers listed in the `testers` command", color=0x00ff00)
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(embed = embed)
    
    @commands.command(name = 'testers', pass_context=True, help = 'Shows a list of beta testers')
    @commands.cooldown(1,5, commands.BucketType.user)
    async def testers(self, ctx):
        embed = discord.Embed(title = "Thank you to everyone listed here!", description = "BETA TESTERS: \n\nBananaBoopCrackers#2002 \nFinnick The Fennec Fox#4334 \nMurdecoi#3541 \nNexivis#8546 \nNootTheNewt#0060 \nSia#3027 \n:six_pointed_star:Mrs-copper-pp:scorpius:#2688 \nMay The Red Panda Cat#8986 \nNitrax#8972 \nRag Darkheart#5080 \nruby_rose_wolf#0568 \nSkipper#6968 \nSugerrion#4086 \nTyler Furrison#2454", color=0x00ff00)
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(embed = embed)
    
    @commands.command(name = 'ping', pass_context=True, help= 'Shows the bot latency connecting to discord.')
    @commands.cooldown(1,5, commands.BucketType.user)
    async def ping(self,ctx):
        ping = self.bot.latency * 1000
        embed = discord.Embed(title = "Pong!", description = '___Took {0}'.format(round(ping, 1)) + "ms___" , color=0x00ff00)
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(embed = embed)

    @commands.command(name = 'invite', pass_context=True, help= 'Shows the bot\'s invite.')
    @commands.cooldown(1,5, commands.BucketType.user)
    async def invite(self,ctx):
        embed = discord.Embed(title = "Here ya go!", description = "My invite is https://furrycentr.al/add" , color=0x00ff00)
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(embed = embed)
    
    @commands.command(name = 'avatar', pass_context=True, help= 'Shows the profile picture of a mentioned user.', aliases=["pfp"])
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.guild_only()
    async def avatar(self,ctx, user : discord.Member):
        embed = discord.Embed(title = f"{user.display_name}'s Profile Picture", color=0x00ff00)
        embed.set_image(url = user.avatar_url)
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(embed = embed)

    @commands.command(name = 'serverinfo', pass_context= True, help='Shows information about the current guild')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def serverinfo(self,ctx):
        embed = discord.Embed(title=ctx.message.guild.name, color=0x00ff00)
        embed.add_field(name="Owner", value=ctx.message.guild.owner, inline=False)
        embed.add_field(name="Date of creation", value=ctx.message.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
        embed.add_field(name="Region", value=ctx.message.guild.region, inline=False)
        embed.set_thumbnail(url = ctx.message.guild.icon_url)
        return await ctx.message.channel.send(embed=embed)
    
    @commands.command(name = 'userinfo', pass_context= True, help='Shows information about the current guild', aliases = ['profile'])
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def userinfo(self,ctx, user: discord.Member):
        rolelist = ''
        for role in user.roles:
            rolelist = rolelist + role.mention + " "
        embed = discord.Embed(description = str(user.name) + "#" +str(user.discriminator) , color = 0x00ff00)
        embed.set_thumbnail(url = user.avatar_url)
        embed.add_field(name = "Name:", value = user.display_name, inline = False)
        embed.add_field(name='Account Created', value=user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline = False)
        embed.add_field(name = "Date Joined:", value=user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline = False)
        embed.add_field(name = "Roles:", value=rolelist, inline = False)
        return await ctx.message.channel.send(embed=embed)

    @commands.command(name='report', pass_context = True, help='Report a bug to the bot\'s developers')
    @commands.guild_only()
    @commands.cooldown(1,120, commands.BucketType.user)
    async def report(self, ctx, *report):
        text = ""
        url = ""
        for str in report:
            text = text + str + ' '
        if ctx.message.attachments:
            for att in ctx.message.attachments:
                text = text + "\n " + att.url
                url = att.url
        channel = self.bot.get_channel(767155058344460298)
        embed = discord.Embed(title="Bug report", description= f'Sent by: {ctx.message.author.name}#{ctx.message.author.discriminator} ({ctx.message.author.id}) \n\nServer Name: \n{ctx.message.guild.name} \n\nReport: \n{text}', color=0x00ff00)
        embed.set_footer(text = f'Channel Name: {ctx.message.channel.name} ({ctx.message.channel.id}) - Wynter 2.0')
        embed.set_image(url = url)
        await channel.send("@here",embed=embed)
        embed = discord.Embed(title = "Report sent!", description = "Thanks for your report! \n\nA developer will contact you if needed." , color=0x00ff00)
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        await ctx.send(ctx.message.author.mention, embed = embed)
    
    @commands.command(name='feedback', pass_context = True, help='Send feedback to the bot\'s developers')
    @commands.guild_only()
    @commands.cooldown(1,120, commands.BucketType.user)
    async def feedback(self, ctx, *report):
        text = ""
        url = ""
        for str in report:
            text = text + str + ' '
        if ctx.message.attachments:
            for att in ctx.message.attachments:
                text = text + "\n " + att.url
                url = att.url
        channel = self.bot.get_channel(785175435075649558)
        embed = discord.Embed(title="Feedback", description= f'Sent by: {ctx.message.author.name}#{ctx.message.author.discriminator} ({ctx.message.author.id}) \n\nServer Name: \n{ctx.message.guild.name} \n\nReport: \n{text}', color=0x00ff00)
        embed.set_footer(text = f'Channel Name: {ctx.message.channel.name} ({ctx.message.channel.id}) - Wynter 2.0')
        embed.set_image(url = url)
        await channel.send("@here",embed=embed)
        embed = discord.Embed(title = "Feedback sent!", description = "Thanks for your feedback! \n\nA developer will contact you if needed." , color=0x00ff00)
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        await ctx.send(ctx.message.author.mention, embed = embed)


def setup(bot):
    bot.add_cog(Info(bot))