#This program asks the user for a number then prints 
#a list of all the divisors of that number. I'll use lists, 
#conditionals, and user input. Early semester refresher :) 
#8/26/25

class Divisors:
    def __init__(self, user_num=None):
        self.user_num = user_num

    def prompt(self):
        invalid_input = True
        while invalid_input:
            user_text = input("Hello! Enter a number and I will return all of the divisors of it: ")
            if user_text.isdigit():
                self.user_num = int(user_text)
                return int(self.user_num)
            else:
                print("You must enter a valid integer.")
    
    def divisor(self):
        for i in range(1, self.user_num + 1): #no need to consider 0 
            if (self.user_num) % (i) == 0:
                print(i)
            
obj = Divisors()
obj.prompt()
obj.divisor()