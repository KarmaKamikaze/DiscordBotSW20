class RPS:
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"

    def get_choices(self):
        return (self.ROCK, self.PAPER, self.SCISSORS)

    def check_win(self, user1_choice, user2_choice):
        # user1 is first parameter, user2 is second
        winner_check = {
            (RPS.ROCK, RPS.PAPER): False,
            (RPS.ROCK, RPS.SCISSORS): True,
            (RPS.PAPER, RPS.ROCK): True,
            (RPS.PAPER, RPS.SCISSORS): False,
            (RPS.SCISSORS, RPS.ROCK): False,
            (RPS.SCISSORS, RPS.PAPER): True,
        }

        won = None
        if user1_choice == user2_choice:
            won = None
        else:
            won = winner_check[(user1_choice, user2_choice)]

        return won
