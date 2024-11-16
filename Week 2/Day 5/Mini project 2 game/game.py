import random

class Game:
    def __init__(self):
        self.choice = ["r","p","s"]

    def get_user_item(self): #Keep asking until the user has selected one of the items – use data validation and looping.
        while True:    #loop
            user_item = input('Select (r)ock, (p)aper or (s)cissors:').lower()
            if user_item in self.choice:
                return user_item
            else: 
                print('Invalid input, choose "r","p" or "s"')

    def get_computer_item(self): # random from list
        return random.choice(self.choice)

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return 'draw'

        if user_item == "r" and computer_item == "s": # possible results
            return 'win'
        if user_item == "p" and computer_item == "r":
            return 'win'
        if user_item == "s" and computer_item == "p":
            return 'win'
        else:
            return 'loss'

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()

        result = self.get_game_result(user_item, computer_item) # comparing
        print(f'You chose: {user_item}. The computer chose: {computer_item}. Result: {result}')
        return result
