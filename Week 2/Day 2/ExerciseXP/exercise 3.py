# Exercise 3 : Dogs Domesticated

from exercisesw2d2 import Dog
import random

class Petdog(Dog):
    def __init__(self, name, age, weight,trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark)
        self.trained = True
    
    def play(self,*args):
        dogs=[dog.name for dog in args]
        print(f'{','.join(dogs)} are playing')

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f'{self.name} does a barrel roll',
                f'{self.name} stands on his back legs',
                f'{self.name} shakes your hand',
                f'{self.name} plays dead'
            ]
            print(random.choice(tricks))
        else:
            print(f'{self.name} is not trained')


dog1 = Petdog('Cody',3,15)
dog2 = Petdog('Tata',4,10)
dog3 = Petdog('Kashtan',3,20)

dog1.train()
dog1.do_a_trick()