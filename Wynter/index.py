# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

import pymysql.cursors
import json
import sys, traceback
import time
import random
import asyncio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
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


def get_prefix(bot,msg):
    try:
        connection = connecttodb()
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `prefix` FROM `guilds` WHERE `id`=%s"
            cursor.execute(sql, (msg.guild.id,))
            result = cursor.fetchone()
            result = json.dumps(result,sort_keys=True)
            result = json.loads(result)
            prefix = result['prefix']
            connection.close()
            return commands.when_mentioned_or(prefix)(bot,msg)
    except Exception as err:
        print(err)
        prefix = '!'
        return commands.when_mentioned_or(prefix)(bot,msg)
        
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=get_prefix, case_insensitive = True, intents = intents)

@client.command(name='prefix', help= 'Sets server prefix')
@commands.has_guild_permissions(manage_guild = True)
async def test(ctx, prefix):
    try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                sql = "UPDATE guilds SET `prefix` = %s WHERE `id`=%s"
                cursor.execute(sql, (prefix,ctx.guild.id,))
                connection.commit()
                sql = "SELECT `prefix` from guilds WHERE `id`=%s"
                cursor.execute(sql, (ctx.guild.id,))
                result = cursor.fetchone()
                result = json.dumps(result,sort_keys=True)
                result = json.loads(result)
                prefix = result['prefix']
                return await ctx.send(f"My prefix has now been set to {prefix}")
    except Exception as err:
        print(err)
        prefix = '!'
        return await ctx.send(f"My current prefix is {prefix} - I was unable to change it at this time. \nError: {err}")

@client.event
async def on_command(ctx):
    blacklistedids = [703382839491821568, 782770244174610432, 763107932753362995, 717428892205580408]
    if ctx.author.id in blacklistedids:
        await ctx.author.send("You are banned from using this bot.")
        return
    

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    while True:
        statuses = [discord.Activity(name='the snow fall | mention me for help!', type=discord.ActivityType.watching), discord.Activity(name='with the snow | mention me for help!', type=discord.ActivityType.playing), discord.Activity(name='people hug | mention me for help!', type=discord.ActivityType.watching), discord.Activity(name='RetroPi games | mention me for help!', type=discord.ActivityType.playing), discord.Activity(name='the kitchen burn | mention me for help!', type=discord.ActivityType.watching),discord.Activity(name='cookies bake in the oven | mention me for help!', type=discord.ActivityType.watching)]
        activity = random.choice(statuses)
        await client.change_presence(activity=activity)
        print(f'changed status to {activity.name}')
        await asyncio.sleep(120)

@client.event
async def on_message(msg):
    if msg.content.lower()== 'f':
        if msg.author.bot:
            return
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT * from guilds WHERE `id`=%s"
                cursor.execute(sql, (msg.guild.id,))
                result = cursor.fetchone()
                result = json.dumps(result,sort_keys=True)
                result = json.loads(result)
                data = result['enablefandx']
                data2 = result['enfandximages']
                if data == 1 and data2 == 1:
                    embed = discord.Embed(title = "Respects have been paid!", description = f"{msg.author.mention} has paid respects" , color=0x00ff00)
                    embed.set_image(url = "https://i.imgur.com/hOnGcgu.png")
                    connection.close()
                    return await msg.channel.send(embed = embed)
                if data == 1 and data2 == 0:
                    connection.close()
                    return await msg.channel.send("Thanks for paying respects", reference = msg)
        except Exception as err:
            print(err)
    if msg.content.lower()== 'x':
        if msg.author.bot:
            return
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT * from guilds WHERE `id`=%s"
                cursor.execute(sql, (msg.guild.id,))
                result = cursor.fetchone()
                result = json.dumps(result,sort_keys=True)
                result = json.loads(result)
                data = result['enablefandx']
                data2 = result['enfandximages']
                if data == 1 and data2 == 1:
                    embed = discord.Embed(title = "Serious doubts are to be had!", description = f"{msg.author.mention} very much has doubts about this." , color=0x00ff00)
                    embed.set_image(url = "https://i.kym-cdn.com/entries/icons/mobile/000/023/021/e02e5ffb5f980cd8262cf7f0ae00a4a9_press-x-to-doubt-memes-memesuper-la-noire-doubt-meme_419-238.jpg")
                    connection.close()
                    return await msg.channel.send(embed = embed)
                if data == 1 and data2 == 0:
                    connection.close()
                    return await msg.channel.send("I agree with you. Doubts are to be had.", reference = msg)
        except Exception as err:
            print(err)

    #Wolf Pack Stuff
    if "http" in msg.content and msg.guild.id == 793961645856391169 or "www." in msg.content and msg.guild.id == 793961645856391169:
        role = discord.utils.get(msg.guild.roles, id= 795455494755975178)
        if role in msg.author.roles:
            return
        if "tenor.com" in msg.content or "cdn.disccordapp.com"  in msg.content or "discord.com" in msg.content or "youtube.com" in msg.content or "google.com" in msg.content or "giphy.com" in msg.content or "spotify.com" in msg.content or "roblox.com" in msg.content or "t.me" in msg.content or "twitter.com" in msg.content or "instagram.com" in msg.content :
            return
        else:
            await msg.delete()
            msg = await msg.channel.send(f"Hey {msg.author.mention}, links aren't allowed in this discord unless specifically approved. Thanks! \n\nThis message will self-destruct in 10 seconds.")
            await asyncio.sleep(10)
            await msg.delete()
    
    #Club Floof Stuff
    
    if "http" in msg.content and msg.guild.id == 725201209358549012 or "www." in msg.content and msg.guild.id == 725201209358549012:
        role = discord.utils.get(msg.guild.roles, id= 783683964232663090)
        if role in msg.author.roles:
            return
        if "tenor.com" in msg.content or "cdn.disccordapp.com"  in msg.content or "discord.com" in msg.content or "toyhou.se" in msg.content or "reddit.com" in msg.content or "youtube.com" in msg.content or "google.com" in msg.content or "giphy.com" in msg.content or "spotify.com" in msg.content or "roblox.com" in msg.content or "t.me" in msg.content or "twitter.com" in msg.content or "instagram.com" in msg.content :
            return
        if msg.channel.id == 783684199311605760 or msg.channel.id == 794719795957202944 or msg.channel.id == 794720350343790632:
            return
        else:
            await msg.delete()
            msg = await msg.channel.send(f"Hey {msg.author.mention}, links aren't allowed in this discord unless specifically approved. Thanks! \n\nThis message will self-destruct in 10 seconds.")
            await asyncio.sleep(10)
            await msg.delete()
    if msg.author.bot and msg.channel.id == 783684179203981332 or msg.author.bot and msg.channel.id == 783684180197507092:
        if msg.author.id == 159985870458322944 or msg.author.id == 339254240012664832 or msg.author.id == 772205583536881694 or msg.author.id == 785054742698393620:
            return
        if "Bot messages aren't allowed here" in msg.content:
            return
        if "links aren't allowed in this discord" in msg.content:
            return
        if "__VOTE TIME__" in msg.content:
            return
        if msg.content == "Thanks for paying respects":
            return
        if msg.content == "I agree with you. Doubts are to be had.":
            return
        await msg.delete()
        msg = await msg.channel.send("Hey! Bot messages aren't allowed here! \n\nIf in error, please ignore this. \n\nThis message will self destruct in 5 seconds.")
        await asyncio.sleep(5)
        await msg.delete()
    if msg.author.bot:
        return

    if msg.content== f"<@!{client.user.id}>":
        try:
            connection = connecttodb()
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `prefix` from guilds WHERE `id`=%s"
                cursor.execute(sql, (msg.guild.id,))
                result = cursor.fetchone()
                result = json.dumps(result,sort_keys=True)
                result = json.loads(result)
                prefix = result['prefix']
                connection.close()
                return await msg.channel.send(f"My prefix is currently `{prefix}` in this guild. \n\nFor help, type `{prefix}help`")
        except Exception as err:
            print(err)
            return await msg.channel.send("I could not get the prefix at this time. Most likely a database error occured. Please try `!`")

    
    await client.process_commands(msg)

initial_extensions = ['info', 'fun', 'meme', 'moderation', 'nsfw', 'christmas', 'fursona']

if __name__ == "__main__":
    for extension in initial_extensions:
        try:
            client.load_extension('cogs.'+ extension)
        except Exception as e:
            exc = '{}:{}'.format(type(e).__name__,e)
            print('Failed to load extension {}\n{}'.format(extension,exc))

@client.event
async def on_message_delete(message):
    if message.author.bot:
        return
    embed = discord.Embed(title = "Message Deleted!", description = f"{message.content}" , color=0x00ff00)
    embed.set_footer(text = f'Wynter 2.0 | Message sent by {message.author.display_name}')
    channel = discord.utils.get(message.guild.text_channels, name='message_logs')
    await channel.send(embed = embed)

@client.event
async def on_bulk_message_delete(messages):
    t = time.time()
    f = open(f"{t}.txt", "w+")
    for message in messages:
        f.write(f"Message: \n{message.content} \nAuthor: \n{message.author} \nChannel: \n{message.channel}\n\n")
    f.close()
    f = open(f"{t}.txt", "r")
    channel = discord.utils.get(messages[0].guild.text_channels, name='message_logs')
    await channel.send("Messages were purged. Here's the log.", file = discord.File(f))
    f.close()
    os.remove(f"{t}.txt")



@client.event
async def on_message_edit(oldmessage, newmessage):
    if oldmessage.author.bot:
        return
    embed = discord.Embed(title = "Message Edited!", description = f"Original Message: \n{oldmessage.content} \n\nNew Message: \n{newmessage.content}" , color=0x00ff00)
    embed.set_footer(text = f'Wynter 2.0 | Message sent by {oldmessage.author.display_name}')
    channel = discord.utils.get(oldmessage.guild.text_channels, name='message_logs')
    await channel.send(embed = embed)

@client.event
async def on_member_ban(guild, user):
    await asyncio.sleep(5)
    entries = await guild.audit_logs(limit=1, action=discord.AuditLogAction.ban).flatten()
    event = entries[0]
    embed = discord.Embed(title = "Member Banned!", description = f"{user.name} was banned by {event.user.display_name} \n\nReason given: \n{event.reason}" , color=0x00ff00)
    embed.set_footer(text = f'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
    channel = discord.utils.get(guild.text_channels, name='case_logs')
    await channel.send(embed = embed)

@client.event
async def on_member_unban(guild, user):
    embed = discord.Embed(title = "Member Ban Revoked!", description = f"{user.name} has had their ban revoked!" , color=0x00ff00)
    embed.set_footer(text = f'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
    channel = discord.utils.get(guild.text_channels, name='case_logs')
    await channel.send(embed = embed)

@client.event
async def on_guild_channel_delete(channel):
    embed = discord.Embed(title = "Guild Channel Deleted!", description = f"Channel: {channel.name}" , color=0x00ff00)
    embed.set_footer(text = f'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
    channel = discord.utils.get(channel.guild.text_channels, name='channel_logging')
    await channel.send(embed = embed)

@client.event
async def on_guild_channel_create(channel):
    embed = discord.Embed(title = "Guild Channel Created!", description = f"Channel: {channel.mention}" , color=0x00ff00)
    embed.set_footer(text = f'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
    channel = discord.utils.get(channel.guild.text_channels, name='channel_logging')
    await channel.send(embed = embed)

@client.event
async def on_guild_join(guild):
    try:
        connection = connecttodb()
        with connection.cursor() as cursor:
            # Read a single record
            sql = "INSERT INTO `guilds` (id,name) VALUES (%s, %s)"
            cursor.execute(sql, (guild.id,guild.name,))
            connection.commit()
            sql = "SELECT `prefix` from guilds WHERE `id`=%s"
            cursor.execute(sql, (guild.id,))
            result = cursor.fetchone()
            result = json.dumps(result,sort_keys=True)
            result = json.loads(result)
            prefix = result['prefix']
            connection.close()
            return print(f"Sucess! Added {guild.name} to the database with a prefix of {prefix}!")
    except Exception as err:
        print(f"{err} when adding {guild.name} to the database")

@client.event
async def on_guild_update(before,after):
    if before.name == after.name:
        return
    try:
        connection = connecttodb()
        with connection.cursor() as cursor:
            # Read a single record
            sql = "UPDATE `guilds` SET `name` = %s WHERE `id` = %s"
            cursor.execute(sql, (after.id,after.name,))
            connection.commit()
            sql = "SELECT `prefix` from guilds WHERE `id`=%s"
            cursor.execute(sql, (after.id,))
            result = cursor.fetchone()
            result = json.dumps(result,sort_keys=True)
            result = json.loads(result)
            prefix = result['prefix']
            connection.close()
            return print(f"Sucess! Updated {after.name} in the database with a prefix of {prefix}!")
    except Exception as err:
        print(f"{err} when updating {after.name} in the database")

@client.event
async def on_guild_remove(guild):
    try:
        connection = connecttodb()
        with connection.cursor() as cursor:
            # Read a single record
            sql = "DELETE FROM `guilds` WHERE `id` = %s"
            cursor.execute(sql, (guild.id,))
            connection.commit()
            connection.close()
            return print(f"Sucess! Removed {guild.name} from the database!")
    except Exception as err:
        print(f"{err} when removing {guild.name} from the database")

@client.event
async def on_guild_channel_update(before, after):
    if not before.topic == after.topic:
        embed = discord.Embed(title = "Channel Topic Edited!", description = f"Previous Topic: \n{before.topic} \n\nNew Topic:\n{after.topic} \n" , color=0x00ff00)
        embed.set_footer(text = f'Wynter 2.0 | Made by Darkmane Arweinydd#0069 | Channel: {after.name}')
        channel = discord.utils.get(before.guild.text_channels, name='channel_logging')
        await channel.send(embed = embed)

    if not before.name == after.name:
        embed = discord.Embed(title = "Channel Name Edited!", description = f"Previous Name: \n{before.name} \n\nNew Name:\n{after.name} ({after.mention}) \n" , color=0x00ff00)
        embed.set_footer(text = f'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        channel = discord.utils.get(before.guild.text_channels, name='channel_logging')
        await channel.send(embed = embed)

@client.event
async def on_member_join(user):
    if user.guild.id == 754816860133916822:
        channel = discord.utils.get(user.guild.text_channels, name='register')
        embed = discord.Embed(title = "Hi there!", description = f"Hey {user.display_name}! Please register to the chat by typing `!register` in chat :)" , color=0x00ff00)
        embed.set_footer(text = f'{user.name}#{user.discriminator} | Made by Darkmane Arweinydd#0069')
        await channel.send(f"{user.mention}", embed = embed)

    embed = discord.Embed(title = "Member joined!", description = f"{user.display_name} has joined the guild" , color=0x00ff00)
    embed.set_footer(text = f'{user.name}#{user.discriminator} | Made by Darkmane Arweinydd#0069')
    channel = discord.utils.get(user.guild.text_channels, name='user_logs')
    await channel.send(embed = embed)

@client.event
async def on_member_remove(user):
    embed = discord.Embed(title = "Member left!", description = f"{user.display_name} has left the guild." , color=0x00ff00)
    embed.set_footer(text = f'{user.name}#{user.discriminator} | Made by Darkmane Arweinydd#0069')
    channel = discord.utils.get(user.guild.text_channels, name='user_logs')
    await channel.send(embed = embed)

@client.event
async def on_member_update(before, after):
    role = discord.utils.get(before.guild.roles, id= 754820807896596520)

    if role not in before.roles and role in after.roles:
        embed = discord.Embed(title = "Welcome!", description = f"{after.mention} has joined! \n\nPlease welcome them to the guild! \n\nFeel free to get some roles from <#756597666011676742>" , color=0x00ff00)
        embed.set_footer(text = 'New Member! | Made by Darkmane Arweinydd#0069')
        channel = discord.utils.get(before.guild.text_channels, id= 754816860133916825)
        await channel.send("<@&755152376700076032>",embed = embed)
        

    cvar = False
    changed = ""
    if not before.display_name == after.display_name:
        print ("Name Change")
        cvar = True
        changed = changed + f"User display name changed!\n\n New name:\n{after.display_name} \nOld name:\n{before.display_name}\n\n"
    if not len(before.roles) == len(after.roles):
        print("Roles change")
        cvar = True
        changed = changed + f"User roles changed!\n\n Old Roles:\n"
        for role in before.roles:
            changed = changed + role.mention
        changed = changed + "\n\nNew Roles:\n"
        for role in after.roles:
            changed = changed + role.mention
    if cvar == True:
        embed = discord.Embed(title = "User Info Updated!", description = f"{after.mention} \n\n{changed}" , color=0x00ff00)
        embed.set_thumbnail(url = after.avatar_url)
        embed.set_footer(text = f'{after.name}#{after.discriminator} | Made by Darkmane Arweinydd#0069')
        channel = discord.utils.get(before.guild.text_channels, name='user_logs')
        await channel.send(embed = embed)

@client.event
async def on_reaction_add(reaction, user):
    embed = discord.Embed(title = "Reaction Added!", description = f"Reaction added by {user.mention} \n\n{reaction.emoji}" , color=0x00ff00)
    embed.set_thumbnail(url = user.avatar_url)
    embed.set_footer(text = f'{user.name}#{user.discriminator} | Made by Darkmane Arweinydd#0069')
    channel = discord.utils.get(reaction.message.guild.text_channels, name='reaction_logging')
    await channel.send(embed = embed)

@client.event
async def on_reaction_remove(reaction, user):
    embed = discord.Embed(title = "Reaction Removed!", description = f"Reaction removed by {user.mention} \n\n{reaction.emoji}" , color=0x00ff00)
    embed.set_thumbnail(url = user.avatar_url)
    embed.set_footer(text = f'{user.name}#{user.discriminator} | Made by Darkmane Arweinydd#0069')
    channel = discord.utils.get(reaction.message.guild.text_channels, name='reaction_logging')
    await channel.send(embed = embed)

@client.event
async def on_user_update(before, after):
    changed = ""
    if not before.avatar_url == after.avatar_url:
        print ("Avatar Change")
        changed = changed + f"User avatar changed!\n\n [Reverse Image Search](https://images.google.com/searchbyimage?image_url={after.avatar_url})\n\n"
    if not before.name == after.name:
        print ("Name Change")
        changed = changed + f"User name changed!\n\n New name:\n{after.name} \nOld name:\n{before.name}\n\n"
    if not before.discriminator == after.discriminator:
        print("Discriminator change")
        changed = changed + f"User discriminator changed!\n\n Old Discriminator:\n #{before.discriminator} \nNew Discriminator: \n#{after.discriminator}"
    for guild in client.guilds:
        if guild.get_member(before.id) is not None:
            embed = discord.Embed(title = "User Info Updated!", description = f"{after.mention} \n\n{changed}" , color=0x00ff00)
            embed.set_footer(text = f'{after.name}#{after.discriminator} | Made by Darkmane Arweinydd#0069')
            channel = discord.utils.get(guild.text_channels, name='user_logs')
            if "User avatar changed" in changed:
                channel = discord.utils.get(guild.text_channels, name='pfp_logging')
                embed.set_image(url = after.avatar_url)
            else:
                embed.set_thumbnail(url = after.avatar_url)
            await channel.send(embed = embed)
            
                

@client.event
async def on_resumed():
    print('reconnected')

@client.event
async def on_command_error(ctx,err):
    if isinstance(err, commands.errors.CommandOnCooldown):
        if ctx.message.author.id == 512608629992456192:
            await ctx.reinvoke()
            return
        embed = discord.Embed(title = "Cooldown!", description = f"You cannot run the following command: `{ctx.message.content}` \n\nas it is currently on cooldown - try again in {err.retry_after} seconds!" , color=0x00ff00)
        embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(embed = embed, reference = ctx.message)
    if isinstance(err, commands.errors.NSFWChannelRequired):
        embed = discord.Embed(title = "Bad Furry!", description = f"You cannot run the following command: `{ctx.message.content}` \n\nin a SFW channel!" , color=0x00ff00)
        embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(embed = embed, reference = ctx.message)
    if isinstance(err, commands.MissingPermissions):
        embed = discord.Embed(title = "No Permission!", description = f"You lack the permissions to run the following command: \n\n{ctx.message.content}" , color=0x00ff00)
        embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(embed = embed, reference = ctx.message)
    if "prefix" in ctx.message.content:
        if isinstance(err, commands.MissingRequiredArgument):
            embed = discord.Embed(title = "Missing argument!", description = f"Hey, to set a prefix, you need to type {ctx.message.content} <prefix>! \n\nTo find the current guild prefix, just mention me!" , color=0x00ff00)
        embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(embed = embed, reference = ctx.message)
    if isinstance(err, commands.MissingRequiredArgument):
            embed = discord.Embed(title = "Missing argument!", description = "Hey, you're missing an argument in this command! \n\nCommands like hug are executed like !hug <user(s)>" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(embed = embed, reference = ctx.message)
client.run(TOKEN, reconnect = True)