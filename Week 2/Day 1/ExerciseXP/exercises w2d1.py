#Exercise 1: Cats

# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age
        
# cat1=Cat('Puff',13)
# cat2=Cat('Spooky',15)
# cat3=Cat('Alice',7)
# cats=[cat1,cat2,cat3]

# def oldest(cats):
#     oldest_cat=cats[0]
#     for k_age in cats:
#         if k_age.age > oldest_cat.age:
#             oldest_cat=k_age
#     return oldest_cat

# oldest_cat=oldest(cats)
# print(oldest_cat.name,oldest_cat.age)

#Exercise 2 : Dogs

# class Dog:
    # def __init__(self,dog_name,dog_height):
#         self.name = dog_name
#         self.height = dog_height

#     def bark(self):
#         return f'{self.name} goes woof!'

#     def jump(self):
#         x = self.height*2
#         return f'{self.name} jumps {x} cm high!'

# davids_dog=Dog('Rex',50)
# print(davids_dog.name)
# print(davids_dog.height)
# print(davids_dog.bark())
# print(davids_dog.jump())

# sarahs_dog=Dog('Teacup',20)
# print(sarahs_dog.name)
# print(sarahs_dog.height)
# print(sarahs_dog.bark())
# print(sarahs_dog.jump())

# if davids_dog.height>sarahs_dog.height:
#     print('Rex is bigger')
# else:
#     print('Teacup is bigger')


# Exercise 3 : Who’s the song producer?

# class Song:
#     def __init__(self,lyrics):
#         self.lyrics = list(lyrics)

#     def sing_me_a_song(self):
#         print('\n'.join(self.lyrics))

# stairway=Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song()


#Exercise 4 : Afternoon at the Zoo

# class Zoo:
#     def __init__(self,zoo_name):
#         self.name = zoo_name
#         self.animals = []

#     def add_animal(self,new_animal):
#         if new_animal not in self.animals:
#             self.animals.append(new_animal)
#         return self.animals
    
#     def get_animals(self):
#         for i,animal in enumerate(self.animals):
#             print(f'Animal # {i+1}: {animal}')
#         return self.animals
    
#     def sell_animal(self,animal_sold):
#         if animal_sold in self.animals:
#             self.animals.remove(animal_sold)
#         else:
#             print(f'{animal_sold} not found')
    
#     def sort_animals(self):
#         groups={}
#         for animal in self.animals:
#             first_l=animal[0].upper()
#             if first_l not in groups:
#                 groups[first_l]=[]
#             groups[first_l].append(animal)

#         for letter in groups:   
#             groups[letter].sort()
        
#         return groups

#     def get_groups(self):
#         sorted_groups=self.sort_animals()
#         for letter,group in sorted_groups.items():
#             print(f'{letter}:{','.join(group)}')

        
# Ramat_gan_zoo=Zoo("Ramat Gan")
# Ramat_gan_zoo.add_animal('Ape')
# Ramat_gan_zoo.add_animal('Babbon')
# Ramat_gan_zoo.add_animal('Bear')
# Ramat_gan_zoo.add_animal('Emu')
# Ramat_gan_zoo.add_animal("Cat")
# Ramat_gan_zoo.add_animal("Cougar")
# Ramat_gan_zoo.add_animal("Eel")


# Ramat_gan_zoo.get_animals()
# Ramat_gan_zoo.sell_animal('Baboon')
# Ramat_gan_zoo.get_animals()
# Ramat_gan_zoo.get_groups()


# Ramat_gan_safari=Zoo('Ramat Gan Safari')
# Ramat_gan_safari.add_animal('Giraffe')
# Ramat_gan_safari.get_animals()


