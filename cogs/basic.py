import discord
from discord.ext import commands
from utils import notify_user


class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, exception):
        print(exception)
        await ctx.send(
            "Please check !help for tips on how to use this command or ask an administrator."
        )

    @commands.command(
        brief="Creates an invite-link for the current channel, which will last for 1 day"
    )
    @commands.guild_only()
    async def invite(self, ctx):
        link = await ctx.channel.create_invite(max_valid_days=1)
        await ctx.send(link)

    @commands.command(
        description=".poke @someGuy.",
        brief="Sends a DM to whoever you mention, telling them they have been poked by you.",
    )
    async def poke(self, ctx, member: discord.Member = None):
        if member is not None:
            message = "%s poked you!" % ctx.author.name
            await notify_user(member, message)
        else:
            await ctx.send("Please use @mention to poke someone.")


def setup(bot):
    bot.add_cog(Basic(bot))
