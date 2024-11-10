#Instructions : Old MacDonald’s Farm

class Farm:
    def __init__(self,farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self,new_animal,count=1):
        if new_animal in self.animals:
            self.animals[new_animal]+= count
        else:
            self.animals[new_animal]=count

    
    def get_info(self):
        print(f"\n{self.name}'s farm")
        for animal in sorted(self.animals.keys()):
            print(f'{animal}:{self.animals[animal]}')
        print('E-I-E-I-0!')
        
    def get_animal_types(self):
        return sorted(self.animals.keys())
    
    def get_short_info(self):
        types=macdonalds.get_animal_types()
        print(f"{self.name}'s farm has {types}")
        
    
macdonalds = Farm("McDonald")
macdonalds.add_animal('cow',5)
macdonalds.add_animal('sheep')
macdonalds.add_animal('sheep')
macdonalds.add_animal('goat', 12)
print(macdonalds.get_info())
print(macdonalds.get_animal_types())
print(macdonalds.get_short_info())    