import random
from discord.ext import commands


class Gambling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="!flip", brief="Flips a coin.")
    async def coinflip(self, ctx):
        number = random.randint(0, 1)
        await ctx.send("Heads" if number == 1 else "Tails")

    @commands.command(
        description="!roll", brief="Rolls a random number between 1 and 100."
    )
    async def roll(self, ctx):
        # Random number from 1-100
        number = random.randrange(1, 101)
        await ctx.send(number)

    @commands.command(
        description="!dice 4\n!dice 6\n!dice 8\n!dice 10\n!dice 12",
        brief="Rolls a d20 unless another die is specified.",
    )
    async def dice(self, ctx, dice_sides=20):
        number = random.randrange(1, dice_sides)
        await ctx.send(number)


def setup(bot):
    bot.add_cog(Gambling(bot))
