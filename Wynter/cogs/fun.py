import aiohttp
import asyncio
import mimetypes
import json
import discord
from discord.ext import commands
import random

class Fun(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(name = 'hug', pass_context=True, help = 'Hug a user', aliases=['hugs', 'cuddle', 'hold'])
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def hug(self, ctx, *, hugged):
        data = ""
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(ctx.message.author.mention, embed = embed) 
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrycentr.al/sfw/hug/") as resp:
                data = await resp.text()
                data = json.loads(data)
        if ctx.message.author in ctx.message.mentions:
            embed = discord.Embed(title = "Hug!", description = f"{self.bot.user.mention} pulls {hugged} into a giant hug! \n\nPS: I'm here for you", color=0x00ff00)
            embed.set_image(url = data["result"]["imgUrl"])
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(embed = embed)
        
        if self.bot.user in ctx.message.mentions:
            embed = discord.Embed(title = "Y..you hugged me?", description = f"Nobody ever hugs me, {ctx.message.author.mention}.. Not even my own dad. Thank you <3", color=0x00ff00)
            embed.set_image(url = data["result"]["imgUrl"])
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(embed = embed)

        embed = discord.Embed(title = "Hug!", description = f"{ctx.message.author.mention} pulls {hugged} into a giant hug!", color=0x00ff00)
        embed.set_image(url = data["result"]["imgUrl"])
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(embed = embed)

    @commands.command(name = 'kiss', pass_context=True, help = 'Kiss a user')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def kiss(self, ctx, *, kissed):
        data = ""
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(ctx.message.author.mention, embed = embed) 
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrycentr.al/sfw/kiss") as resp:
                data = await resp.text()
                data = json.loads(data)
        if ctx.message.author in ctx.message.mentions:
            embed = discord.Embed(title = "Kiss!", description = f"{self.bot.user.mention} pulls {kissed} close to them and kisses them on the cheek! \n\nPS: I'm here for you", color=0x00ff00)
            embed.set_image(url = data["result"]["imgUrl"])
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(embed = embed)
        
        if self.bot.user in ctx.message.mentions:
            embed = discord.Embed(title = "Y..you kissed me?", description = f"Nobody ever shows me love, {ctx.message.author.mention}.. Not even my own dad. Thank you <3", color=0x00ff00)
            embed.set_image(url = data["result"]["imgUrl"])
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(embed = embed)

        embed = discord.Embed(title = "Hug!", description = f"{ctx.message.author.mention} pulls {kissed} close to them and kisses them on the cheek!", color=0x00ff00)
        embed.set_image(url = data["result"]["imgUrl"])
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(embed = embed)

    @commands.command(name = 'glomp', pass_context=True, help = 'Glomp a user')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def glomp(self, ctx, *, glomped):
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(ctx.message.author.mention, embed = embed) 
       
        if ctx.message.author in ctx.message.mentions:
            embed = discord.Embed(title = "Glomp!", description = f"{self.bot.user.mention} tackles {glomped} and pulls them into a giant hug! \n\nPS: I'm here for you", color=0x00ff00)
            embed.set_image(url = "https://i.imgur.com/St7SfOp.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(embed = embed)

        embed = discord.Embed(title = "Glomp!", description = f"{ctx.message.author.mention} tackles {glomped} and pulls them into a giant hug!", color=0x00ff00)
        embed.set_image(url = "https://i.imgur.com/St7SfOp.png")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(embed = embed)
    
    @commands.command(name = 'nuzzle', pass_context=True, help = 'Nuzzle a user')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def nuzzle(self, ctx, *, nuzzled):
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(ctx.message.author.mention, embed = embed) 
       
        if ctx.message.author in ctx.message.mentions:
            embed = discord.Embed(title = "Nuzzle Wuzzle OwO!", description = f"{self.bot.user.mention} snuggles against {nuzzled}, nuzzling into them gently! \n\nPS: I'm here for you", color=0x00ff00)
            embed.set_image(url = "https://i.imgur.com/St7SfOp.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(embed = embed)

        embed = discord.Embed(title = "Nuzzle Wuzzle OwO!", description = f"{ctx.message.author.mention} snuggles against {nuzzled}, nuzzling into them gently!", color=0x00ff00)
        embed.set_image(url = "https://i.imgur.com/St7SfOp.png")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(embed = embed)

    @commands.command(name = 'bite', pass_context=True, help = 'Deprecated')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def bite(self, ctx):
        embed = discord.Embed(title = "Deprecated!", description = "This command has been replaced with the `nibble` command. :)", color=0x00ff00)
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(embed = embed)

    @commands.command(name = 'nibble', pass_context=True, help = 'Nibble on a user\'s ear')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def nibble(self, ctx, *, nibbled):
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(ctx.message.author.mention, embed = embed) 
       
        if ctx.message.author in ctx.message.mentions:
            embed = discord.Embed(title = "Om nom nom!", description = f"{self.bot.user.mention} gently begins to nibble on {nibbled}'s ear! \n\nPS: I'm here for you", color=0x00ff00)
            embed.set_image(url = "https://i.imgur.com/R78kQgT.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(embed = embed)

        embed = discord.Embed(title = "Om nom nom!", description = f"{ctx.message.author.mention} gently begins to nibble on {nibbled}'s ear!", color=0x00ff00)
        embed.set_image(url = "https://i.imgur.com/R78kQgT.png")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(embed = embed)

    @commands.command(name = 'howl', pass_context=True, help = 'Let out a deep howl... awoooooooooooo!')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def howl(self, ctx):
        embed = discord.Embed(title = "Awoooooooo!", description = f"{ctx.message.author.mention} has let out a loud howl. \n\nAwoooooooooooooo!" , color=0x00ff00)
        embed.set_thumbnail(url = "https://i.imgur.com/RKgG0V7.png")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(ctx.message.author.mention, embed = embed)
    
    @commands.command(name = 'rawr', pass_context=True, help = 'Let out a humongus rawr!', aliases= ['roar'])
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def rawr(self, ctx):
        embed = discord.Embed(title = "ROARRRRRR!", description = f"{ctx.message.author.mention} has let out a loud roar, scaring the whole jungle!" , color=0x00ff00)
        embed.set_thumbnail(url = "https://i.imgur.com/DdmisyT.png")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(ctx.message.author.mention, embed = embed)
    
    @commands.command(name = 'blep', pass_context=True, help = 'Do a cute blep!')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def blep(self, ctx):
        embed = discord.Embed(title = "Blep uwu!", description = f"{ctx.message.author.mention} does a blep, looking rather cute as they do so!" , color=0x00ff00)
        embed.set_thumbnail(url = "https://i.imgur.com/XxpnfWX.png")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(ctx.message.author.mention, embed = embed)
    
    @commands.command(name = 'growl', pass_context=True, help = 'Let out a deep growl. Who upset you?')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def growl(self, ctx):
        embed = discord.Embed(title = "Grrrrr!", description = f"{ctx.message.author.mention} has let out a loud growl." , color=0x00ff00)
        embed.set_thumbnail(url = "https://i.imgur.com/on6OpBv.png")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(ctx.message.author.mention, embed = embed)
    
    @commands.command(name = 'rubs', pass_context=True, help = 'Give someone belly rubs')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def rubs(self, ctx, *, rubbed):
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(ctx.message.author.mention, embed = embed) 
       
        if ctx.message.author in ctx.message.mentions:
            embed = discord.Embed(title = "Belly wubs!", description = f"{self.bot.user.mention} notices that {rubbed}'s belly is exposed and gives it rubs, making them kick their leg! \n\nPS: I'm here for you", color=0x00ff00)
            embed.set_image(url = "https://i.imgur.com/L4iyKt9.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(embed = embed)

        embed = discord.Embed(title = "Belly wubs!", description = f"{ctx.message.author.mention} notices that {rubbed}'s belly is exposed and gives it rubs, making them kick their leg!", color=0x00ff00)
        embed.set_image(url = "https://i.imgur.com/L4iyKt9.png")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(embed = embed)
    
    @commands.command(name = 'flop', pass_context=True, help = 'Flop on top of someone')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def flop(self, ctx, *, flopped):
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(ctx.message.author.mention, embed = embed) 
       
        if ctx.message.author in ctx.message.mentions:
            embed = discord.Embed(title = "Flooop!", description = f"{self.bot.user.mention} pounces {flopped} and flops on top of them gently! \n\nPS: I'm here for you", color=0x00ff00)
            embed.set_image(url = "https://i.imgur.com/A2jMwRk.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(embed = embed)

        embed = discord.Embed(title = "Flooop!", description = f"{ctx.message.author.mention} pounces {flopped} and flops on top of them gently!", color=0x00ff00)
        embed.set_image(url = "https://i.imgur.com/A2jMwRk.png")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(embed = embed)
    
    @commands.command(name = 'nap', pass_context=True, help = 'Nap on someone')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def nap(self, ctx, *, napped):
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(ctx.message.author.mention, embed = embed) 
       
        if ctx.message.author in ctx.message.mentions:
            embed = discord.Embed(title = "zzz!", description = f"{ctx.message.author.mention} has fell asleep. Sweet Dreams!", color=0x00ff00)
            embed.set_image(url = "https://i.imgur.com/A2jMwRk.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(embed = embed)

        embed = discord.Embed(title = "zzz!", description = f"{ctx.message.author.mention} lies against {napped} and gently drifts off..", color=0x00ff00)
        embed.set_image(url = "https://i.imgur.com/A2jMwRk.png")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(embed = embed)
    
    @commands.command(name = 'pat', pass_context=True, help = 'Give someone head pats', aliases=['pet', 'pats'])
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def petted(self, ctx, *, petted):
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(ctx.message.author.mention, embed = embed) 
       
        if ctx.message.author in ctx.message.mentions:
            embed = discord.Embed(title = "Pat pat pat!", description = f"{self.bot.user.mention} softly pats {petted}'s head! \n\nPS: I'm here for you", color=0x00ff00)
            embed.set_image(url = "https://i.imgur.com/p2U1kpt.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(embed = embed)

        embed = discord.Embed(title = "Pat pat pat!", description = f"{ctx.message.author.mention} softly pats {petted}'s head!", color=0x00ff00)
        embed.set_image(url = "https://i.imgur.com/p2U1kpt.png")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(embed = embed)
    
    @commands.command(name = 'slap', pass_context=True, help = 'Slap a user')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def slap(self, ctx, *, slapped):
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(ctx.message.author.mention, embed = embed) 

        embed = discord.Embed(title = "Ouch that's gotta hurt!", description = f"{ctx.message.author.mention} goes up to {slapped} and slaps them right across the face, leaving a red mark!", color=0x00ff00)
        embed.set_image(url = "https://i.imgur.com/0JeUUgs.png")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(embed = embed)
    
    @commands.command(name = 'throwdict', pass_context=True, help = 'Throw a dictionary at someone\'s head')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def throwdict(self, ctx, *, injured):
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(ctx.message.author.mention, embed = embed)
        
        if ctx.message.author in ctx.message.mentions:
            embed = discord.Embed(title = "No!", description = "I do not condone self-violence!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(ctx.message.author.mention, embed = embed)

        embed = discord.Embed(title = "Ouch that's gotta hurt!", description = f"{ctx.message.author.mention} eyes up {injured}, before throwing a dictionary at them.", color=0x00ff00)
        embed.set_image(url = "https://i.imgur.com/v4MihL9.jpg")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(embed = embed)
    
    @commands.command(name = 'bap', pass_context=True, help = 'Bap someone\'s nose with a newspaper')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def bap(self, ctx, *, bapped):
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(ctx.message.author.mention, embed = embed)
        
        if ctx.message.author in ctx.message.mentions:
            embed = discord.Embed(title = "No!", description = "I do not condone self-violence!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(ctx.message.author.mention, embed = embed)

        embed = discord.Embed(title = "BAD FURRY", description = f"{ctx.message.author.mention} notices {bapped} being baed, so they bap them with a newspaper.", color=0x00ff00)
        embed.set_image(url = "https://i.imgur.com/CsGfqgc.png")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(embed = embed)
    
    @commands.command(name = 'snug', pass_context=True, help = 'Snuggle a user', aliases=['snuggle'])
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def snug(self, ctx, *, hugged):
        data = ""
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(ctx.message.author.mention, embed = embed) 
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrycentr.al/sfw/hug/") as resp:
                data = await resp.text()
                data = json.loads(data)
        if ctx.message.author in ctx.message.mentions:
            embed = discord.Embed(title = "Snuggle!", description = f"{self.bot.user.mention} pulls {hugged} tight to them, snuggling them close \n\nPS: I'm here for you", color=0x00ff00)
            embed.set_image(url = data["result"]["imgUrl"])
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(embed = embed)
        
        if self.bot.user in ctx.message.mentions:
            embed = discord.Embed(title = "Y..you snuggled with me?", description = f"Nobody ever shows me love, {ctx.message.author.mention}.. Not even my own dad. Thank you <3", color=0x00ff00)
            embed.set_image(url = data["result"]["imgUrl"])
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(embed = embed)

        embed = discord.Embed(title = "Snuggle!", description = f"{ctx.message.author.mention} pulls {hugged} tight to them, snuggling them close", color=0x00ff00)
        embed.set_image(url = data["result"]["imgUrl"])
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(embed = embed)
    

    @commands.command(name = 'ship', pass_context=True, help = 'See how well two users get shipped together!')
    @commands.guild_only()
    @commands.cooldown(1,15, commands.BucketType.user)
    async def ship(self, ctx, user1: discord.Member, user2: discord.Member):
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(ctx.message.author.mention, embed = embed) 
        embed = discord.Embed(title = "Ship!", description = f"{ctx.message.author.mention} has shipped {user1.mention} with {user2.mention}! They got a score of {random.randint(0,100)}", color=0x00ff00)
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(embed = embed)

    @commands.command(name = '8ball', pass_context=True, help = 'Ask the magic 8ball a question..')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def eightball(self, ctx, *, question):
        responses = [
			'As I see it, yes',
			'Ask again later',
			'Better not tell you now',
			'I cannot predict this right now',
			'Concentrate and ask again.',
			'Don’t count on it.',
			'It is certain.',
			'It is decidedly so.',
			'Most likely.',
			'My reply is no.',
			'My sources say no.',
			'Outlook not so good.',
			'Outlook pawsitive.',
			'Reply hazy, try again.',
			'Signs point to yes.',
			'Very doubtful.',
			'Without a doubt.',
			'Yes.',
			'Yes – definitely.',
			'You may rely on it.',
		]
        response = random.choice(responses)
        embed = discord.Embed(title = "The 8 ball has spoken!", description = f"Question: \n{question}\n\nAnswer:\n{response}" , color=0x00ff00)
        embed.set_thumbnail(url = "https://upload.wikimedia.org/wikipedia/commons/9/90/Magic8ball.jpg")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        await ctx.send(embed = embed)
    
    @commands.command(name = 'rp', pass_context=True, help = 'Get a random roleplay scenario!')
    @commands.guild_only()
    @commands.cooldown(1,60, commands.BucketType.user)
    async def rp(self, ctx):
        responses = [
			f'*it was a cold saturday night, {ctx.message.author.mention} was sitting by the fireplace in a lodge, having just came back from a long day of skiing...*',
			'Scenario: you\'re on a beach, relaxing on your towel as you try to get a tan. You think about a dip in the pool, but can you be bothered?',
			f'*it was a Friday night and {ctx.message.author.mention} had just gotten off from a long day at work, sitting at the bar as they ordered a vodka, someone was sitting across from them. Will they say hello?*',
			'Scenario: You and another person have a sleepover that goes wrong. What exactly goes wrong? that is up to you to decide!',
            'You get out of bed and go down to the kitchen to eat a piece of toast. Now you are standing in your kitchen, confused as to why you are here again.'
		]
        response = random.choice(responses)
        await ctx.send("At the moment, I only have 5 scenarios... here's yours! \n\n" + response)

    @commands.command(name = 'boop', pass_context=True, help = 'Boop a user')
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def boop(self, ctx, *, booped):
        data = ""
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(ctx.message.author.mention, embed = embed) 
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrycentr.al/sfw/boop/") as resp:
                data = await resp.text()
                data = json.loads(data)
        if ctx.message.author in ctx.message.mentions:
            embed = discord.Embed(title = "Boop!", description = f"{self.bot.user.mention} goes up to {booped} and boops them right on the nose! \n\nPS: I'm here for you :)", color=0x00ff00)
            embed.set_image(url = data["result"]["imgUrl"])
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(embed = embed)

        embed = discord.Embed(title = "Boop!", description = f"{ctx.message.author.mention} goes up to {booped} and boops them right on the nose!", color=0x00ff00)
        embed.set_image(url = data["result"]["imgUrl"])
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(embed = embed)

    @commands.command(name = 'lick', pass_context=True, help = 'Lick a user', aliases = ['licks'])
    @commands.guild_only()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def lick(self, ctx, *, licked):
        data = ""
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(ctx.message.author.mention, embed = embed)  
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.furrycentr.al/sfw/lick/") as resp:
                data = await resp.text()
                data = json.loads(data)
        if ctx.message.author in ctx.message.mentions:
            embed = discord.Embed(title = "Lick!", description = f"{self.bot.user.mention} pulls {licked} close to them and licks them on the cheek. Aww! \n\nPS: I'm here for you. :)", color=0x00ff00)
            embed.set_image(url = data["result"]["imgUrl"])
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(embed = embed)

        embed = discord.Embed(title = "Lick!", description = f"{ctx.message.author.mention} pulls {licked} close to them and licks them on the cheek. Aww!", color=0x00ff00)
        embed.set_image(url = data["result"]["imgUrl"])
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(embed = embed)
def setup(bot):
    bot.add_cog(Fun(bot))

