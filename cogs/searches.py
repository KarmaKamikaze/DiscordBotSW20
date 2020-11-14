from utils import get_mama_jokes
import aiohttp
import discord
from discord.ext import commands
from utils import text_to_owo
from utils import get_mama_jokes


class Searches(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(description="Provide arguments", brief="The bot will repeat what you typed")
    async def say(self, ctx, *args):
        if len(args) > 0:
            await ctx.send(" ".join(args))
        else:
            await ctx.send("It is not possible to send an empty message.")
    

    @commands.command(brief="Text-to-OwO")
    async def owo(self, ctx):
        await ctx.send(text_to_owo(ctx.message.content[5:]))

    
    @commands.command(brief="Sends a random Yo Mama joke")
    async def yomama(self, ctx, member: discord.Member = None):
        joke = await get_mama_jokes()
        if member is not None:
            await ctx.send("%s, %s" % (member.name, joke))
        else:
            await ctx.send(joke)


    @commands.command(brief="Sends a random cat picture")
    async def randomcat(self, ctx):
        async with ctx.channel.typing(): # Make it look like the bot is typing (functions as a loading bar)
            # Set up a API client session and grab the json result as a temporary file
            async with aiohttp.ClientSession() as cs:
                async with cs.get("http://aws.random.cat/meow") as request:
                    data = await request.json()

                    embed = discord.Embed()
                    embed.set_image(url=data['file'])
                    embed.set_footer(text="http://random.cat/")

                    await ctx.send(embed=embed)
    

    @commands.command(brief="Sends a random dog picture")
    async def randomdog(self, ctx):
        async with ctx.channel.typing(): # Make it look like the bot is typing (functions as a loading bar)
            # Set up a API client session and grab the json result as a temporary file
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://random.dog/woof.json") as request:
                    data = await request.json()

                    embed = discord.Embed()
                    embed.set_image(url=data['url'])
                    embed.set_footer(text="https://random.dog/")

                    await ctx.send(embed=embed)

    

def setup(bot):
    bot.add_cog(Searches(bot))
