from exercisesw2d2 import Family

class TheIncredibles(Family):
    def __init__(self, last_name, members=None):
        super().__init__(last_name, members)

    def use_power(self,name):
        for member in self.members:
            if member['name']==name:
                if member['age']>=18:
                    print(f'{member['name']} use the power: {member['power']}')
                    return
                else:
                    raise ValueError(f'{member['name']} is not old enough to use powers')
        print(f'{name} has no powers')

    def incredible_presentation(self):
        print('*Here is our powerful family*')
        print(f'{self.last_name} family:')
        for member in self.members:
            print(f'Name: {member['name']}, age: {member['age']},gender: {member['gender']}, '
                  f'Power: {member['power']}, Incredible name: {member['incredible_name']},is child: {member['is_child']}')
            
incredible_family = TheIncredibles(
    last_name="Incredibles",
    members=[
        {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
        {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
    ]
)

incredible_family.incredible_presentation()
incredible_family.born(name='Baby Jack',age=1,gender='Male',is_child=True,power='Unknown power',incredible_name='TinyJack')
incredible_family.incredible_presentation()