import discord
from discord.ext import commands
import aiohttp
import asyncio
import json
import os
from dotenv import load_dotenv
import pymysql.cursors

load_dotenv()
DBHOST = os.getenv('DBHOST')
DBUSER = os.getenv('DBUSER')
DBPW = os.getenv('DBPW')
DB = os.getenv('DB')

def connecttodb():
    # Connect to the database
    connection = pymysql.connect(host=DBHOST,
                                user=DBUSER,
                                password=DBPW,
                                db=DB,
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    return connection

class Fursona(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name = 'sona', pass_context=True, help = 'Get a user\'s fursona')
    @commands.cooldown(1,5, commands.BucketType.user)
    async def sona(self, ctx, user:discord.Member):
        connection = connecttodb()
        try:
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT * from `fursonas` WHERE `user_id`=%s"
                cursor.execute(sql, (user.id))
                result = cursor.fetchone()
                result = json.dumps(result,sort_keys=True)
                result = json.loads(result)
                embed = discord.Embed(title = f"{result['name']}", color=0x00ff00)
                embed.add_field(name='Age', value=f"{result['age']}", inline=False)
                embed.add_field(name='Gender (and pronouns)', value=f"{result['gender']}", inline=False)
                embed.add_field(name='Species', value=f"{result['species']}", inline=False)
                embed.add_field(name='Sexuality', value=f"{result['sexuality']}", inline=False)
                embed.add_field(name='Additional Info', value=f"{result['addinfo']}", inline=False)
                embed.set_thumbnail(url = result['pfplink'])
                embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
                await ctx.send(embed=embed, reference = ctx.message)
        except Exception as err:
            print(err)
            err = str(err)
            if "NoneType" in err:
                return await ctx.send("This user does not have a fursona")
            await ctx.send(f"Error fetching fursona! \n\n{err}")

    @commands.command(name = 'register-sona', pass_context=True, help = 'Register a fursona with Wynter')
    @commands.cooldown(1,5, commands.BucketType.user)
    async def registersona(self, ctx):
        if ctx.message.guild.id == 796073346017001504:
            await ctx.send("Registering fursonas has been blacklisted in this guild")
        await ctx.send(f":e_mail: {ctx.message.author.mention} Check your DMs!")
        a = ctx.message.author
        await a.send("Let's set up your fursona! \n\nFirst, may I get their name?")
        await asyncio.sleep(1)
        def check(m):
            return m.author.id == a.id
        msg = await self.bot.wait_for('message', check = check)
        name = msg.content
        await a.send(f"{name}? That's an awesome name! \n\nHow old is {name}?")
        await asyncio.sleep(1)
        msg = await self.bot.wait_for('message', check = check)
        age = 0
        try:
            age = int(msg.content)
        except:
            await ctx.message.author.send("That is an invalid age. \n\nPlease try again or your registration will be aborted.")
            msg = await self.bot.wait_for('message', check = check)
            try:
                age = int(msg.content)
            except:
                await ctx.message.author.send("That is an invalid age. \n\nYour registration has been aborted")
        await a.send(f"Got it, {name} is {age} years old! \n\nMay I ask what species your fursona is?")
        await asyncio.sleep(1)
        msg = await self.bot.wait_for('message', check = check)
        species = msg.content
        await a.send(f"Got it, {name} is a {species}! \n\nMay I know what sexuality your fursona is?")
        await asyncio.sleep(1)
        msg = await self.bot.wait_for('message', check = check)
        sexuality = msg.content
        await a.send(f"Got it, {name} is {sexuality}!\n\nMay I know their gender and preferred pronouns?")
        await asyncio.sleep(1)
        msg = await self.bot.wait_for('message', check = check)
        gender = msg.content
        await a.send(f"Got it, {name} is {gender}\n\nIs there any additional info people should know about {name}? (type no if none)")
        await asyncio.sleep(1)
        msg = await self.bot.wait_for('message', check = check)
        addinfo = msg.content
        if addinfo.lower() == "no":
            addinfo = "N/A"
        await a.send("Got it, next please send me an image of your fursona! (Not a link!) - links will return an error and may terminate your registation.")
        await asyncio.sleep(1)
        msg = await self.bot.wait_for('message', check = check)
        pfplink = ""
        for att in msg.attachments:
            pfplink = att.url
        if pfplink == "":
            await a.send("You have not attached an image! \n\nPlease try again, if I do not get a valid image this time, your registration will be terminated.")
            await asyncio.sleep(1)
            msg = await self.bot.wait_for('message', check = check)
            for att in msg.attachments:
                pfplink = att.url
            if pfplink == "":
                await a.send("You have not attached an image! \n\nYour registration was terminated")
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                sql = "INSERT INTO `fursonas` (user_id, name, age, gender, species, sexuality, addinfo, pfplink) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (a.id, name, age, gender, species, sexuality, addinfo, pfplink))
                connection.commit()
                sql = "SELECT * from `fursonas` WHERE `user_id`=%s and `name`= %s"
                cursor.execute(sql, (a.id, name))
                result = cursor.fetchone()
                result = json.dumps(result,sort_keys=True)
                result = json.loads(result)
                embed = discord.Embed(title = f"{result['name']}", color=0x00ff00)
                embed.add_field(name='Age', value=f"{result['age']}", inline=False)
                embed.add_field(name='Gender (and pronouns)', value=f"{result['gender']}", inline=False)
                embed.add_field(name='Species', value=f"{result['species']}", inline=False)
                embed.add_field(name='Sexuality', value=f"{result['sexuality']}", inline=False)
                embed.add_field(name='Additional Info', value=f"{result['addinfo']}", inline=False)
                embed.set_thumbnail(url = result['pfplink'])
                embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
                await a.send("Here is your fursona!", embed=embed)
        except Exception as err:
            print(err)
            await a.send(f"Error adding fursona! \n\n{err}")
                

def setup(bot):
    bot.add_cog(Fursona(bot))