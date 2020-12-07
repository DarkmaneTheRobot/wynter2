import discord
from discord.ext import commands
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
imgusr = os.getenv('IMGUSR')
imgpw = os.getenv('IMGPW')

class Meme(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name = 'changemymind', pass_context=True, help = 'Generates a change my mind meme using imgur')
    async def changemymind(self, ctx, *data):
        text = ""
        for str in data:
            text = text + str + ' '
        url = f"https://api.imgflip.com/caption_image?text0={text}&username={imgusr}&password={imgpw}&template_id=129242436"
        payload={}
        headers = {
        'Cookie': '__cfduid=d8877b9d3f7f03d74d494201c69a043e81605576645; claim_key=eVrjsNJKFzqzCYRCMTSxdpSh5BnGPLdV'
        }
        response = requests.request("GET", url, headers=headers, data=payload)

        data = json.loads(response.text)
        url = data["data"]["url"]
        return await ctx.send(url)

def setup(bot):
    bot.add_cog(Meme(bot))