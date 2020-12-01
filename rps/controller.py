import random
from .model import RPS


class RPSGame:
    def play(self, user_choice):
        rps_instance = RPS()

        if user_choice not in rps_instance.get_choices():
            raise Exception("User_choice has to be either rock, paper or scissors!")

        bot_choice = random.choice(rps_instance.get_choices())

        won = rps_instance.check_win(user_choice, bot_choice)

        return won, bot_choice
