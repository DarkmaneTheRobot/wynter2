# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

import pymysql.cursors
import json
import sys, traceback

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
DBHOST = os.getenv('DBHOST')
DBUSER = os.getenv('DBUSER')
DBPW = os.getenv('DBPW')
DB = os.getenv('DB')

# Connect to the database
connection = pymysql.connect(host=DBHOST,
                             user=DBUSER,
                             password=DBPW,
                             db=DB,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def get_prefix(bot,msg):
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `prefix` FROM `guilds` WHERE `id`=%s"
            cursor.execute(sql, (msg.guild.id,))
            result = cursor.fetchone()
            result = json.dumps(result,sort_keys=True)
            result = json.loads(result)
            prefix = result['prefix']
            return commands.when_mentioned_or(prefix)(bot,msg)
    except Exception as err:
        print(err)
        prefix = '!'
        return commands.when_mentioned_or(prefix)(bot,msg)
        

client = commands.Bot(command_prefix=get_prefix, case_insensitive = True)

@client.command(name='prefix', help= 'Sets server prefix')
@commands.has_guild_permissions(manage_guild = True)
async def test(ctx, prefix):
    try:
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
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    activity = discord.Activity(name='the beta testers | mention me for help!', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)

@client.event
async def on_message(msg):
    if msg.author.bot:
        return
    if msg.content== 'f':
        try:
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `enablefandx` from guilds WHERE `id`=%s"
                cursor.execute(sql, (msg.guild.id,))
                result = cursor.fetchone()
                result = json.dumps(result,sort_keys=True)
                result = json.loads(result)
                data = result['enablefandx']
                if data == 1:
                    embed = discord.Embed(title = "Respects have been paid!", description = f"{msg.author.mention} has paid respects" , color=0x00ff00)
                    embed.set_image(url = "https://i.imgur.com/hOnGcgu.png")
                    return await msg.channel.send(embed = embed)
        except Exception as err:
            print(err)
    if msg.content== 'x':
        try:
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `enablefandx` from guilds WHERE `id`=%s"
                cursor.execute(sql, (msg.guild.id,))
                result = cursor.fetchone()
                result = json.dumps(result,sort_keys=True)
                result = json.loads(result)
                data = result['enablefandx']
                if data == 1:
                    embed = discord.Embed(title = "Serious doubts are to be had!", description = f"{msg.author.mention} very much has doubts about this." , color=0x00ff00)
                    embed.set_image(url = "https://i.kym-cdn.com/entries/icons/mobile/000/023/021/e02e5ffb5f980cd8262cf7f0ae00a4a9_press-x-to-doubt-memes-memesuper-la-noire-doubt-meme_419-238.jpg")
                    return await msg.channel.send(embed = embed)
        except Exception as err:
            print(err)
    if msg.content== f"<@!{client.user.id}>":
        try:
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT `prefix` from guilds WHERE `id`=%s"
                cursor.execute(sql, (msg.guild.id,))
                result = cursor.fetchone()
                result = json.dumps(result,sort_keys=True)
                result = json.loads(result)
                prefix = result['prefix']
                return await msg.channel.send(f"My prefix is currently `{prefix}` in this guild. \n\nFor help, type `{prefix}help`")
        except Exception as err:
            print(err)
            return await msg.channel.send("I could not get the prefix at this time. Most likely a database error occured. Please try `!`")

    
    await client.process_commands(msg)

initial_extensions = ['info', 'fun', 'meme', 'moderation', 'nsfw']

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
async def on_message_edit(oldmessage, newmessage):
    if oldmessage.author.bot:
        return
    embed = discord.Embed(title = "Message Edited!", description = f"Original Message: \n{oldmessage.content} \n\nNew Message: \n{newmessage.content}" , color=0x00ff00)
    embed.set_footer(text = f'Wynter 2.0 | Message sent by {oldmessage.author.display_name}')
    channel = discord.utils.get(oldmessage.guild.text_channels, name='message_logs')
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
            return print(f"Sucess! Added {guild.name} to the database with a prefix of {prefix}!")
    except Exception as err:
        print(f"{err} when adding {guild.name} to the database")

@client.event
async def on_guild_update(before,after):
    if before.name == after.name:
        return
    try:
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
            return print(f"Sucess! Updated {after.name} in the database with a prefix of {prefix}!")
    except Exception as err:
        print(f"{err} when updating {after.name} in the database")

@client.event
async def on_guild_remove(guild):
    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "DELETE FROM `guilds` WHERE `id` = %s"
            cursor.execute(sql, (guild.id,))
            connection.commit()
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
async def on_command_error(ctx,err):
    if isinstance(err, commands.MissingPermissions):
        embed = discord.Embed(title = "No Permission!", description = f"You lack the permissions to run the following command: \n\n{ctx.message.content}" , color=0x00ff00)
        embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(ctx.message.author.mention,embed = embed)
    if "prefix" in ctx.message.content:
        if isinstance(err, commands.MissingRequiredArgument):
            embed = discord.Embed(title = "Missing argument!", description = f"Hey, to set a prefix, you need to type {ctx.message.content} <prefix>! \n\nTo find the current guild prefix, just mention me!" , color=0x00ff00)
        embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
        embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
        return await ctx.send(ctx.message.author.mention,embed = embed)
    if isinstance(err, commands.MissingRequiredArgument):
            embed = discord.Embed(title = "Missing argument!", description = "Hey, you're missing an argument in this command! \n\nCommands like hug are executed like !hug <user(s)>" , color=0x00ff00)
            embed.set_thumbnail(url = "https://freeiconshop.com/wp-content/uploads/edd/cross-flat.png")
            embed.set_footer(text = 'Wynter 2.0 | Made by Darkmane Arweinydd#0069')
            return await ctx.send(ctx.message.author.mention,embed = embed)
client.run(TOKEN)