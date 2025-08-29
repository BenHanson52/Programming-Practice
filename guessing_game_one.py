#This program has the user guess a number between
#1 and 9, tells them if they're too low or high,
#then terminates when the user guesses the number correctly
import random

class game:
    def __init__(self):
        self.user_guess = None
        self.num = random.randint(1,9)

    @staticmethod
    def welcome_message():
        print("Welcome to the Number Guessing Game. A number will " \
        "be generated between 1 and 9. You get 3 tries to guess correctly.\n"\
        "You'll be told if it's too low or too high. The number has been chosen.")

    def user_input(self):
        self.user_guess = input("Enter a number between 1 and 9: ")

        while not self.user_guess.isdigit() or int(self.user_guess) not in range(1, 10):
            self.user_guess = input("You must enter a number between 1 and 9. Try again: ")

        self.user_guess = int(self.user_guess)
        return self.user_guess

    
    def game_loop(self):
        if self.user_guess > self.num:
            print("Your guess was too high")
            return False
        if self.user_guess < self.num:
            print("Your guess was too low")
            return False
        else:
            print(f'You got it right! The number was {self.num}')
            return True
        
    @staticmethod
    def end_message():
        print("Game Over!")
    
obj = game()
obj.welcome_message()
game_over = False
count = 0
while not game_over:
    obj.user_input()
    game_over = obj.game_loop()
    count+=1
    print(f'You have {3 - count} guesses left.')
    if count >= 3:
        game_over = True
        obj.end_message()


    
