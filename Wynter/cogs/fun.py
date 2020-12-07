import http.client
import mimetypes
import json
import discord
from discord.ext import commands
import random

class Fun(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(name = 'hug', pass_context=True, help = 'Hug a user', aliases=['hugs', 'cuddle'])
    @commands.guild_only()
    async def hug(self, ctx, *hugged):
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(ctx.message.author.mention, embed = embed) 
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
        if ctx.message.author in ctx.message.mentions:
            embed = discord.Embed(title = "Hug!", description = f"{self.bot.user.mention} pulls {htxt} into a giant hug! \n\nPS: I'm here for you", color=0x00ff00)
            embed.set_image(url = data["result"]["imgUrl"])
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(embed = embed)
        
        if self.bot.user in ctx.message.mentions:
            embed = discord.Embed(title = "Y..you hugged me?", description = f"Nobody ever hugs me, {ctx.message.author.mention}.. Not even my own dad. Thank you <3", color=0x00ff00)
            embed.set_image(url = data["result"]["imgUrl"])
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(embed = embed)

        embed = discord.Embed(title = "Hug!", description = f"{ctx.message.author.mention} pulls {htxt} into a giant hug!", color=0x00ff00)
        embed.set_image(url = data["result"]["imgUrl"])
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(embed = embed)
    
    @commands.command(name = 'snug', pass_context=True, help = 'Snuggle a user', aliases=['snuggle'])
    @commands.guild_only()
    async def hug(self, ctx, *hugged):
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(ctx.message.author.mention, embed = embed) 
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
        if ctx.message.author in ctx.message.mentions:
            embed = discord.Embed(title = "Snuggle!", description = f"{self.bot.user.mention} pulls {htxt} tight to them, snuggling them close \n\nPS: I'm here for you", color=0x00ff00)
            embed.set_image(url = data["result"]["imgUrl"])
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(embed = embed)
        
        if self.bot.user in ctx.message.mentions:
            embed = discord.Embed(title = "Y..you snuggled with me?", description = f"Nobody ever shows me love, {ctx.message.author.mention}.. Not even my own dad. Thank you <3", color=0x00ff00)
            embed.set_image(url = data["result"]["imgUrl"])
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(embed = embed)

        embed = discord.Embed(title = "Snuggle!", description = f"{ctx.message.author.mention} pulls {htxt} tight to them, snuggling them close", color=0x00ff00)
        embed.set_image(url = data["result"]["imgUrl"])
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(embed = embed)

    @commands.command(name = 'ship', pass_context=True, help = 'See how well two users get shipped together!')
    @commands.guild_only()
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
    async def eightball(self, ctx, *question):
        q = ""
        for str in question:
            q = q + str + " "
        if q == "":
            embed = discord.Embed(title = "Missing argument!", description = f"Hey, you're missing an argument in this command! \n\nUsage: {ctx.message.content} <question>" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(embed = embed)
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
        embed = discord.Embed(title = "The 8 ball has spoken!", description = f"Question: \n{q}\n\nAnswer:\n{response}" , color=0x00ff00)
        embed.set_thumbnail(url = "https://upload.wikimedia.org/wikipedia/commons/9/90/Magic8ball.jpg")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        await ctx.send(embed = embed)
    
    @commands.command(name = 'rp', pass_context=True, help = 'Get a random roleplay scenario!')
    @commands.guild_only()
    async def rp(self, ctx,):
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
    async def boop(self, ctx, *hugged):
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(ctx.message.author.mention, embed = embed) 
        conn = http.client.HTTPSConnection("api.furrycentr.al")
        payload = ''
        headers = {
        'Cookie': '__cfduid=d9a224e3d8c1cb5402581c2ae57ae3ec21605192790'
        }
        conn.request("GET", "/sfw/boop/", payload, headers)
        res = conn.getresponse()
        data = res.read()
        data = data.decode("utf-8")
        data = json.loads(data)
        htxt = ""
        for str in hugged:
            htxt = htxt + str + ", "
        if ctx.message.author in ctx.message.mentions:
            embed = discord.Embed(title = "Boop!", description = f"{self.bot.user.mention} goes up to {htxt} and boops them right on the nose! \n\nPS: I'm here for you :)", color=0x00ff00)
            embed.set_image(url = data["result"]["imgUrl"])
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(embed = embed)

        embed = discord.Embed(title = "Boop!", description = f"{ctx.message.author.mention} goes up to {htxt} and boops them right on the nose!", color=0x00ff00)
        embed.set_image(url = data["result"]["imgUrl"])
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(embed = embed)

    @commands.command(name = 'lick', pass_context=True, help = 'Hug a user', aliases = ['licks'])
    @commands.guild_only()
    async def lick(self, ctx, *hugged):
        if len(ctx.message.mentions) > 3:
            embed = discord.Embed(title = "Too many mentions!", description = "Too many mentions! You can only mention 3 people at a time!" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(ctx.message.author.mention, embed = embed)  
        conn = http.client.HTTPSConnection("api.furrycentr.al")
        payload = ''
        headers = {
        'Cookie': '__cfduid=d9a224e3d8c1cb5402581c2ae57ae3ec21605192790'
        }
        conn.request("GET", "/sfw/lick/", payload, headers)
        res = conn.getresponse()
        data = res.read()
        data = data.decode("utf-8")
        data = json.loads(data)
        htxt = ""
        for str in hugged:
            htxt = htxt + str + ", "
        if ctx.message.author in ctx.message.mentions:
            embed = discord.Embed(title = "Lick!", description = f"{self.bot.user.mention} pulls {htxt} close to them and licks them on the cheek. Aww! \n\nPS: I'm here for you. :)", color=0x00ff00)
            embed.set_image(url = data["result"]["imgUrl"])
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(embed = embed)

        embed = discord.Embed(title = "Lick!", description = f"{ctx.message.author.mention} pulls {htxt} close to them and licks them on the cheek. Aww!", color=0x00ff00)
        embed.set_image(url = data["result"]["imgUrl"])
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(embed = embed)
def setup(bot):
    bot.add_cog(Fun(bot))

