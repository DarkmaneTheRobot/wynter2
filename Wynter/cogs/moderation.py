import discord
from discord.ext import commands
from discord.utils import get
import time
import random
import os
from dotenv import load_dotenv
import json

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

class Moderation(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command(name = 'kick', pass_context=True, help = 'Kicks a user')
    @commands.has_guild_permissions(kick_members = True)
    async def kick(self, ctx, user:discord.Member,*data):
        await ctx.message.delete()
        if user.id == ctx.message.author.id:
            embed = discord.Embed(title = "Lolwut!", description = "Are you sure you want to punish yourself?" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(embed=embed)
        reason = ""
        for txt in data:
            reason = reason + txt + ' '
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                guild = ctx.message.guild
                sql = "INSERT INTO `punishments` (servername, serverid, offender, moderator, type, reason, offenderid) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (guild.name,guild.id,user.display_name,ctx.message.author.display_name,"KICK", reason, str(user.id)))
                connection.commit()
                print(f"Sucess! Added a punishment to {user.display_name}!")
                connection.close()
        except Exception as err:
            print(f"{err} when adding a punishment for {user.display_name} to the database")
        embed = discord.Embed(title = "Kicked!", description = f"You have been kicked from {ctx.message.guild.name}! \n\nReason given:\n{reason}" , color=0x00ff00)
        embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        try:
            await user.send(embed=embed)
        except Exception as e:
            print(e)
        await user.kick()
        embed = discord.Embed(title = "Kicked!", description = f"{ctx.message.author.display_name} has kicked {user.display_name}! \n\nReason given:\n{reason}" , color=0x00ff00)
        embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        channel = discord.utils.get(ctx.message.guild.text_channels, name='case_logs')
        await channel.send(embed=embed)
        

    @commands.command(name = 'ban', pass_context=True, help = 'Bans a user')
    @commands.has_guild_permissions(ban_members= True)
    async def ban(self, ctx, user:discord.Member,*data):
        await ctx.message.delete()
        if user.id == ctx.message.author.id:
            embed = discord.Embed(title = "Lolwut!", description = "Are you sure you want to punish yourself?" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(embed=embed)
        reason = ""
        for txt in data:
            reason = reason + txt + ' '
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                guild = ctx.message.guild
                sql = "INSERT INTO `punishments` (servername, serverid, offender, moderator, type, reason, offenderid) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (guild.name,guild.id,user.display_name,ctx.message.author.display_name,"BAN", reason, str(user.id)))
                connection.commit()
                print(f"Sucess! Added a punishment to {user.display_name}!")
                connection.close()
        except Exception as err:
            print(f"{err} when adding a punishment for {user.display_name} to the database")
        embed = discord.Embed(title = "Banned!", description = f"You have been banned from {ctx.message.guild.name}! \n\nReason given:\n{reason}" , color=0x00ff00)
        embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        try:
            await user.send(embed=embed)
        except Exception as e:
            print(e)
        await user.ban()
        embed = discord.Embed(title = "Banned!", description = f"{ctx.message.author.display_name} has banned {user.display_name}! \n\nReason given:\n{reason}" , color=0x00ff00)
        embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        channel = discord.utils.get(ctx.message.guild.text_channels, name='case_logs')
        await channel.send(embed=embed)
        
    
    @commands.command(name = 'hackban', pass_context=True, help = 'Bans user(s) that aren\'t in the guild.')
    @commands.has_guild_permissions(ban_members= True)
    @commands.cooldown(1,120, commands.BucketType.user)
    async def hackban(self, ctx,*ids):
        await ctx.message.delete()
        if len(ids) > 50:
            embed = discord.Embed(title = "Lol no.", description = "Try mentioning less than 50 IDs. (Austin, i'm looking at you)" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(embed=embed)
        
        bannedusers = 0
        
        for users in ids:
            if users == "!hackban":
                print("no user")
            else:
                bannedusers = bannedusers +1
                print(users)
                user = await self.bot.fetch_user(int(users))
                await ctx.message.guild.ban(user)

        channel = discord.utils.get(ctx.message.guild.text_channels, name='case_logs')
        embed = discord.Embed(title = "Hackbanned, get out of here, ya dirty trolls.", description = f"{ctx.message.author.display_name} Hackbanned {bannedusers} user(s)" , color=0x00ff00)
        embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        await channel.send(embed=embed)
        
    
    @commands.command(name = 'warn', pass_context=True, help = 'Warns a user')
    @commands.has_guild_permissions(kick_members = True)
    async def warn(self, ctx, user:discord.Member,*data):
        await ctx.message.delete()
        if user.id == ctx.message.author.id:
            embed = discord.Embed(title = "Lolwut!", description = "Are you sure you want to punish yourself?" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(embed=embed)
        reason = ""
        for txt in data:
            reason = reason + txt + ' '
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                guild = ctx.message.guild
                sql = "INSERT INTO `punishments` (servername, serverid, offender, moderator, type, reason, offenderid) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (guild.name,guild.id,user.display_name,ctx.message.author.display_name,"WARN", reason, str(user.id)))
                connection.commit()
                print(f"Sucess! Added a punishment to {user.display_name}!")
                connection.close()
        except Exception as err:
            print(f"{err} when adding a punishment for {user.display_name} to the database")
        embed = discord.Embed(title = "Warned!", description = f"You have been warned on {ctx.message.guild.name}! \n\nReason given: \n{reason}" , color=0x00ff00)
        embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        await user.send(embed=embed)
        embed = discord.Embed(title = "Warned!", description = f"{ctx.message.author.display_name} has warned {user.mention}! \n\nReason given: \n{reason}" , color=0x00ff00)
        embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        channel = discord.utils.get(ctx.message.guild.text_channels, name='case_logs')
        await channel.send(embed=embed)
       
    
    @commands.command(name = 'purge', pass_context=True, help = 'Purges x amount of messages', aliases = ['clear', 'clean'])
    @commands.has_guild_permissions(kick_members = True)
    async def purge(self, ctx, amount: int):
        amount = amount + 1
        if amount > 100:
            amount = 100
        await ctx.message.channel.purge(limit = amount, check = lambda msg: not msg.pinned)
        embed = discord.Embed(title = "Messages Purged!", description = f"{ctx.message.author.display_name} has deleted {amount} messages from {ctx.message.channel.mention}!" , color=0x00ff00)
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        channel = discord.utils.get(ctx.message.guild.text_channels, name='message_logs')
        await channel.send(embed=embed)
        channel = discord.utils.get(ctx.message.guild.text_channels, name='case_logs')
        await channel.send(embed=embed)
    
    @commands.command(name = 'lookup', pass_context=True, help = 'see a user\'s punishments')
    @commands.has_guild_permissions(kick_members = True)
    async def lookup(self, ctx, user: discord.Member):
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT * FROM `punishments` WHERE `offenderid`=%s AND serverid = %s"
                cursor.execute(sql, (user.id, ctx.message.guild.id))
                result = cursor.fetchall()
                result = json.dumps(result,sort_keys=True)
                result = json.loads(result)
                punishments = ""
                pcount = 0
                for p in result:
                    pcount = pcount +1 
                    punishments = punishments + "**" + p['type'] + "**" + ": " + p['reason'] + "\n\nGiven by: \n" + p['moderator'] + "\n\n"
            embed = discord.Embed(title = f"{user.display_name}'s punishments!", description = punishments , color=0x00ff00)
            embed.set_footer(text = f'Wynter 2.0 | Made by Darkmane Arweinydd#0069 | {pcount} total punishments')
            connection.close()
            return await ctx.send(embed=embed)
        except Exception as err:
            print(err)
            return await ctx.send(f"an error occured - {err} - this user may have no punishments recorded")

    @commands.command(name = 'mute', pass_context=True, help = 'Mutes a user')
    @commands.has_guild_permissions(kick_members = True)
    async def mute(self, ctx, user:discord.Member,*data):
        await ctx.message.delete()
        if user.id == ctx.message.author.id:
            embed = discord.Embed(title = "Lolwut!", description = "Are you sure you want to punish yourself?" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(embed=embed)
        reason = ""
        for txt in data:
            reason = reason + txt + ' '
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                guild = ctx.message.guild
                sql = "INSERT INTO `punishments` (servername, serverid, offender, moderator, type, reason, offenderid) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (guild.name,guild.id,user.display_name,ctx.message.author.display_name,"MUTE", reason, str(user.id)))
                connection.commit()
                print(f"Sucess! Added a punishment to {user.display_name}!")
                connection.close()
        except Exception as err:
            print(f"{err} when adding a punishment for {user.display_name} to the database")
        embed = discord.Embed(title = "Muted!", description = f"You have been muted on {ctx.message.guild.name}! \n\nReason given: \n{reason}" , color=0x00ff00)
        embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        try:
            await user.send(embed=embed)
        except Exception as e:
            print(e)
        muted = discord.utils.get(ctx.message.guild.roles, name = "Muted")
        await user.add_roles(muted)
        embed = discord.Embed(title = "Warned!", description = f"{ctx.message.author.display_name} has muted {user.mention}! \n\nReason given: \n{reason}" , color=0x00ff00)
        embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        channel = discord.utils.get(ctx.message.guild.text_channels, name='case_logs')
        await channel.send(embed=embed)
       


def setup(bot):
    bot.add_cog(Moderation(bot))