from utils import get_mama_jokes
import discord
from discord.ext import commands
from utils import get_mama_jokes


class Searches(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(brief="Sends a random Yo Mama joke")
    async def yomama(self, ctx, member: discord.Member = None):
        joke = await get_mama_jokes()
        if member is not None:
            await ctx.send("%s, %s" % (member.name, joke))
        else:
            await ctx.send(joke)
    

def setup(bot):
    bot.add_cog(Searches(bot))
