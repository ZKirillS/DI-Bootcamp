# Exercise 1: Currencies

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        if self.amount==1 or self.amount==-1:
            return f'{self.amount} {self.currency}'
        else:
            return f'{self.amount} {self.currency}s'
   

    def __int__(self):
        return self.amount

    def __repr__(self):
        if self.amount==1 or self.amount==-1:
            return f'{self.amount} {self.currency}'
        else:
            return f'{self.amount} {self.currency}s'

    def __add__(self,other):
        if isinstance(other,Currency):
            if self.currency != other.currency:
                raise ValueError('Cannot add different currencies.')
            return Currency(self.currency, self.amount + other.amount)
        elif isinstance(other,int):
            return Currency(self.currency,self.amount+other)
        else:
            raise TypeError('Unsupported type for addition')


        


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print(repr(c1))
print(c1+5)
print(c1+c2)
print(c1)
c1+=5
print(c1)
c1+=c2
print(c1)
c1+c3
print(c1)



# Exercise 2: Import
from func import summary as sm

sm(5,16)


# Exercise 3: String module
import string
import random
random_string = ''.join(random.choices(string.ascii_letters,k=5))
print(random_string)


# Exercise 4 : Current Date
import datetime
def current_date():
    return datetime.date.today()

print(current_date())

# Exercise 5 : Amount of time left until January 1s

def time_left():
    current = datetime.datetime.now()
    next_date = datetime.datetime(2025,1,1)
    time_1 = next_date - current
    days = time_1.days
    seconds = time_1.seconds

    hours = seconds//3600
    minutes = (seconds % 3600) // 60
    seconds_left = seconds % 60

    return f'1st January is in {days} days, {hours} hours, {minutes} minutes, and {seconds_left} seconds'

print(time_left())

# Exercise 6 : Birthday and minutes

def bday_minutes(birthday_str):
    b_day = datetime.datetime.strptime(birthday_str,'%Y-%m-%d')
    today = datetime.datetime.now()
    d_lived= today - b_day
    minutes = d_lived.total_seconds() / 60
    return f'You have lived {int(minutes)} minutes'

birthday_input = input()
print(bday_minutes(birthday_input))

# Exercise 7 : Faker Module
from faker import Faker
fake = Faker()

users = []

def add_new_user(**kwargs):
        users.append(kwargs)
  
def addding():
      add_new_user(name=fake.name(),address=fake.address(),language_code=fake.language_code())
      
      
addding()
print(users)
addding()
addding()
print(users)