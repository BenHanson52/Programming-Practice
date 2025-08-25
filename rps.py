#8/25 python refresher practice. 
#Rock Paper Scissors game that loops in the case of a tie.
import random

class RPS:
    def __init__(self, user_guess=None, robot_guess=None, game_over=False):
        self.user_guess = user_guess
        self.robot_guess = robot_guess
        self.game_over = game_over

    @staticmethod
    def welcome():
        print("Hello, welcome to the Rock Paper Scissors Game. The game will loop until you win.")

    def user_input(self):
        choices = ["rock", "paper", "scissors"]
        while self.user_guess not in choices:
            self.user_guess = input("Select your choice by typing in Rock, Paper, or Scissors:").lower().strip()
            return self.user_guess
            
    def robot_input(self):
        options = [ "rock", "paper", "scissors"]
        self.robot_guess = random.choice(options)
        
    def gameplay(self, user_guess, robot_guess):
        match(user_guess, robot_guess):
            case user, robot if user == robot:
                return "It's a tie! Play Again."
            case "paper", "rock":
                self.game_over = True
                return f'You win with paper! The robot guessed {self.robot_guess}. Game Over.'
            case "rock", "scissors":
                self.game_over = True
                return f'You win with rock! The robot guessed {self.robot_guess}. Game Over'
            case "scissors", "paper":
                self.game_over = True
                return f'You win with scissors! The robot guessed {self.robot_guess}. Game Over.'
            case _:
                self.game_over = True
                return f'The robot beat your guess of {self.user_guess} with {self.robot_guess}. Game Over.'

game = RPS()
game.welcome()
game.user_input()
game.robot_input()
print(game.gameplay(game.user_guess, game.robot_guess))
while not game.game_over:
    game.user_guess = None
    game.user_input()
    print(game.gameplay(game.user_guess, game.robot_guess))

