import discord
from discord.ext import commands
from discord.utils import get
import time
import random
import os
from dotenv import load_dotenv
import json
import asyncio
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

    @commands.command(name = 'register', pass_context=True, help = 'Register for Floof Paradise! (only works in guild)')
    async def register(self, ctx):
        if not ctx.message.guild.id == 754816860133916822:
            return
        await ctx.send(f":e_mail: {ctx.message.author.mention} Check your DMs!")
        a = ctx.message.author
        await a.send("Hi there, welcome to the Floof Paradise registration. \n\nDuring this process, please do not send any messages to servers Wynter is in, or it may see it as answers to your questions.\n\nTo start, I get your fursona name or a name you prefer to be called?")
        def check(m):
            return m.author.id == a.id
        await asyncio.sleep(1)
        msg = await self.bot.wait_for('message', check = check)
        name = msg.content
        await a.send(f"Hi {name} - May I next get your age?")
        await asyncio.sleep(1)
        msg = await self.bot.wait_for('message', check = check)
        age = 0
        agebracket = ""
        try:
            age = int(msg.content)
        except:
            await ctx.message.author.send("That is an invalid age. \n\nPlease try again or your registration will be aborted.")
            await asyncio.sleep(1)
            msg = await self.bot.wait_for('message', check = check)
            try:
                age = int(msg.content)
            except:
                await ctx.message.author.send("That is an invalid age. \n\nYour registration has been aborted")
        if age <= 13:
            await a.send("You are underaged. According to discord TOS, users under 13 are not allowed to use the application. Read more here \n\nhttps://discord.com/terms")
            await ctx.message.guild.ban(a, reason = "Underaged user, banned due to TOS violation.")
            return
        if age >= 18:
            agebracket = "Adult"
        if age < 18:
            agebracket = "Minor"
        await a.send(f"Thanks, to protect your age, you will be shown as a {agebracket} in the server. \n\nNext, may I know what gender you identify as and your preferred pronouns?")
        await asyncio.sleep(1)
        msg = await self.bot.wait_for('message', check = check)
        gender = msg.content
        await a.send(f"Got it, you refer to yourself as {gender} \n\nNext, would you like to be mentioned in the server for things such as important announcements? (YES/NO)")
        await asyncio.sleep(1)
        msg = await self.bot.wait_for('message', check = check)
        announcementpref = msg.content
        await a.send("Got it, next, may I ask if it's okay for users to DM you? (YES/NO/ASK)")
        await asyncio.sleep(1)
        msg = await self.bot.wait_for('message', check = check)
        dmpref = msg.content
        await a.send("Finally, tell me about your fursona. \n\nWhat species are they? What's their favourite activites? What gender are they? Do they like sleeping all day? Anything! \n\nNote: if you don't have a fursona, tell us info of what you imagine your fursona to be!")
        await asyncio.sleep(1)
        msg = await self.bot.wait_for('message', check = check)
        fursonainfo = msg.content

        embed = discord.Embed(title = "Registration!", description = f"{a.mention}'s Registration" , color=0x00ff00)
        embed.set_thumbnail(url = a.avatar_url)
        embed.add_field(name='Preferred Name', value=f"{name}", inline=False)
        embed.add_field(name='Age', value=f"{agebracket}", inline=False)
        embed.add_field(name='Gender and Pronouns', value=f"{gender}", inline=False)
        embed.add_field(name='Fursona Info', value=f"{fursonainfo}", inline=False)
        embed.add_field(name='Okay to mention?', value=f"{announcementpref}", inline=False)
        embed.add_field(name='Okay to DM?', value=f"{dmpref}", inline=False)
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        channel = discord.utils.get(ctx.message.guild.text_channels, name='introductions')
        await channel.send("<@&754817901428604929>")
        await channel.send(embed=embed)
        await a.send("Thank you! Your registration has been sent to a staff member for review. \n\nThey'll accept you as soon as possible!")



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
            await user.send(embed=embed, file = discord.File("./saygoodbye.mp4"))
        except Exception as e:
            print(e)
        await user.ban(reason = reason)
        embed = discord.Embed(title = "Banned!", description = f"{ctx.message.author.display_name} has banned {user.display_name}! \n\nReason given:\n{reason}" , color=0x00ff00)
        embed.set_thumbnail(url = "https://image.freepik.com/free-photo/judge-gavel-hammer-justice-law-concept_43403-625.jpg")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        channel = discord.utils.get(ctx.message.guild.text_channels, name='case_logs')
        await channel.send(embed=embed)
    
    @commands.command(name = 'remind', pass_context=True, help = 'Set a reminder')
    @commands.cooldown(1,120, commands.BucketType.user)
    async def remind(self, ctx, minutes: float, *, reminder):
        embed = discord.Embed(title = f"{minutes} minute reminder!", description = f"I have set a reminder to remind you about {reminder} - check your DMs soon!" , color=0x00ff00)
        minutes = minutes * 60
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        await ctx.send(embed= embed, reference = ctx.message)
        await asyncio.sleep(minutes)
        embed = discord.Embed(title = "Your Reminder", description = f"{reminder}" , color=0x00ff00)
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        await ctx.message.author.send(embed = embed)
    
    @commands.command(name = 'hackban', pass_context=True, help = 'Bans user(s) that aren\'t in the guild.')
    @commands.has_guild_permissions(ban_members= True)
    @commands.cooldown(1,120, commands.BucketType.user)
    async def hackban(self, ctx,*ids):
        try:
            await ctx.message.delete()
        except Exception as e:
            await ctx.send("Failed deleting the command message. It is strongly reccomended to give the bot manage messages permission to do this.")
        if len(ids) > 50:
            embed = discord.Embed(title = "Lol no.", description = "Try mentioning less than 50 IDs. (Austin, i'm looking at you)" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(embed=embed)
        
        bannedusers = 0
        bannedlist = ""
        for user in ids:
            if user == "!hackban":
                print("no user")
            else:
                try:
                    bannedlist = bannedlist + user + ", "
                    bannedusers = bannedusers +1
                    print(user)
                    u = await self.bot.fetch_user(int(user))
                    await ctx.message.guild.ban(u, reason = f"Hackbanned by {ctx.message.author.display_name}")
                except Exception as e:
                    print(f"Exception: {e}")
                    await ctx.send("Error banning {user} - " + e)

        await ctx.send(f"Banned IDS: \n\n{bannedlist}")
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