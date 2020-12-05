import random
from discord.ext import commands
from hangman.controller import HangmanGame
from rps.controller import RPSGame
from rps.model import RPS
from rps.parser import rock_paper_scissors_parser

# Hangman variables
hangman_games = {}
word = "discord"
user_guesses = list()


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
        game_instance = RPSGame()
        user_choice = user_choice.choice

        won, bot_choice = game_instance.play(user_choice)

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
            message = "It's a draw! You both chose %s." % user_choice

        await ctx.send(message)

    @commands.command(
        description="!hangman d",
        brief="Start a game of hangman.",
        usage="!hangman [character] or [word]",
        aliases=["hm"],
    )
    async def hangman(self, ctx, user_guess: str):
        player_id = ctx.author.id
        hangman_instance = HangmanGame()
        game_over, won = hangman_instance.run(player_id, user_guess)

        if game_over:
            game_over_message = "You lost! You did not guess the word."
            if won:
                game_over_message = "You won! You guessed the word!"
            game_over_message = (
                game_over_message
                + "\nThe word was %s." % hangman_instance.get_secret_word()
            )
            await hangman_instance.reset(player_id)
            await ctx.send(game_over_message)
        else:
            await ctx.send(
                "Progress: %s\nGuesses so far: %s"
                % (
                    hangman_instance.get_progress_string(),
                    hangman_instance.get_guess_string(),
                )
            )


def setup(bot):
    bot.add_cog(Gambling(bot))
