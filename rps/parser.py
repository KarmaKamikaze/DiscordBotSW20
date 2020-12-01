from .model import RPS


class rock_paper_scissors_parser:
    def __init__(self, choice):
        choice = choice.lower()

        if choice == RPS.ROCK:
            self.choice = RPS.ROCK
        elif choice == RPS.PAPER:
            self.choice = RPS.PAPER
        elif choice == RPS.SCISSORS:
            self.choice = RPS.SCISSORS
        else:
            raise Exception("RPS ERROR!")