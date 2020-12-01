import random
from discord.ext import commands
from rps.model import RPS
from rps.parser import rock_paper_scissors_parser


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

    @commands.command(
        description="!rps scissors. Defaults to rock.",
        brief="Play a game of Rock, Paper, Scissors against the bot.",
        usage="rock | paper | scissors",
    )
    # Defaults to rock by setting the user_choice equal to another parser instance of RPS.ROCK
    async def rps(
        self,
        ctx,
        user_choice: rock_paper_scissors_parser = rock_paper_scissors_parser(RPS.ROCK),
    ):
        rps_model = RPS()
        bot_choice = random.choice(rps_model.get_choices())
        user_choice = user_choice.choice

        # User is first parameter, bot is second
        winner_check = {
            (RPS.ROCK, RPS.PAPER): False,
            (RPS.ROCK, RPS.SCISSORS): True,
            (RPS.PAPER, RPS.ROCK): True,
            (RPS.PAPER, RPS.SCISSORS): False,
            (RPS.SCISSORS, RPS.ROCK): False,
            (RPS.SCISSORS, RPS.PAPER): True,
        }

        won = None
        if bot_choice == user_choice:
            won = None
        else:
            won = winner_check[(user_choice, bot_choice)]

        if won is True:
            message = "You win: %s beats %s!" % (
                user_choice.title(),
                bot_choice.title(),
            )
        elif won is False:
            message = "You lose: %s does not beat %s!" % (
                user_choice.title(),
                bot_choice.title(),
            )
        else:
            message = "It's a draw!"

        await ctx.send(message)


def setup(bot):
    bot.add_cog(Gambling(bot))
