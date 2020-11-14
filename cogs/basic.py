from discord.ext import commands
from utils import text_to_owo

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, exception):
        print(exception)
        await ctx.send("Please check !help for tips on how to use this command or ask an administrator.")

    
    @commands.command(description="Provide arguments", brief="The bot will repeat what you typed")
    async def say(self, ctx, *args):
        if len(args) > 0:
            await ctx.send(" ".join(args))
        else:
            await ctx.send("It is not possible to send an empty message.")
    

    @commands.command(brief="Text-to-OwO")
    async def owo(self, ctx):
        await ctx.send(text_to_owo(ctx.message.content[5:]))

    
    @commands.command(brief="Creates an invite-link for the current channel, which will last for 1 day")
    @commands.guild_only()
    async def invite(self, ctx):
        link = await ctx.channel.create_invite(max_valid_days=1)
        await ctx.send(link)
    

def setup(bot):
    bot.add_cog(Basic(bot))
