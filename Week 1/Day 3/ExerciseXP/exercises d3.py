list1 = [1,2,3]
list2 = ['a','b','c']
list3 = [1.1, 2.2, 3.3, 4.4, 5.5]

for item in zip(list1, list2, list3): # only go as far it is possible
    print(item)
print(list(zip(list1,list2,list3)))
print(dict(zip(list2,list1)))

# Exercise 1 : Convert lists into dictionaries
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
print(dict(zip(keys,values)))

# Exercise 2 : Cinemax #2

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost = 0
for member, age in family.items():
    if age < 3:
        cost = 0 
    elif 3 <= age <= 12:
        cost = 10 
    else:
        cost = 15
    
    print(f"{member} has to pay ${cost}")
    total_cost += cost

print(f"Total cost:{total_cost}")

# Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).

f_names = []
f_ages = []
family_ma={}
ticket = 0
total_cost = 0
keep_asking = True
while keep_asking :
    q1 = input('Please enter the first name of the attendee: ')
    q2 = input('Please enter the age of this person: ')
    q3 = input("type exit ")
    f_names.append(q1)
    f_ages.append(q2)
    family_ma[q1] = q2
    print(family_ma)
    if q3=='exit':
        keep_asking = False
        print(f'here is the total: {ticket} USD')
    else:
        qn = int(q2)
    if qn < 3:
        price = 0
        ticket += price
    elif 3<= qn <=12:
        price = 10
        ticket += price
    elif qn > 12:
        price = 15
        ticket += price
    else:
        print('Invalid entry. Only full years.')
    ticket += price
    print(f'{f_names}, aged {f_ages}, paying {price}.')


# Exercise 3: Zara
# name: Zara 
# creation_date: 1975 
# creator_name: Amancio Ortega Gaona 
# type_of_clothes: men, women, children, home 
# international_competitors: Gap, H&M, Benetton 
# number_stores: 7000 
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green

brand={'name':'Zara','creation_date':1975, 
    'creator_name':'Amancio Ortega Gaona', 
    'type_of_clothes':[{'men','women','children','home'}],
    'international_competitors':[{'Gap','H&M','Benetton'}],
    'number_stores':7000,'major_color':{'France':'blue',
    'Spain':'red','US':{'pink','green'}}}

# Change the number of stores to 2.
brand['number_stores']=2

# Print a sentence that explains who Zaras clients are.
print(f"Zara's clients are {brand['type_of_clothes'][0]} from all over the world")

# Add a key called country_creation with a value of Spain.
brand['country_creation']= 'Spain'


# Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
if 'Desidual' not in brand.items():
    brand['international_competitors'].append('Desidual')

# Delete the information about the date of creation.
del brand['creation_date']
print(brand)
# Print the last international competitor.
print(brand['international_competitors'][-1])

# Print the major clothes colors in the US.
print(brand['major_color']['US'])

# # Print the amount of key value pairs (ie. length of the dictionary).
print({len(brand)})
# # Print the keys of the dictionary.
print(brand.keys())
# # Create another dictionary called more_on_zara with the following details:
more_on_zara={'creation_date':1975,'number_stores':10000}
# # creation_date: 1975 
# # number_stores: 10 000
brand.update(more_on_zara)
print(brand)
# # 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
# # 14. Print the value of the key number_stores. What just happened ?
print(brand['number_stores'])


#Exercise 4 : Disney characters

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
numbers=[]
for i in range(0,10):
    numbers.append(i)
print(dict(zip(users,numbers)))

# #Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
print(dict(zip(numbers,users)))

# #Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
print(users.sort())
print(dict(zip(users,numbers)))

#Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
# The characters, which names start with the letter “m” or “p”.

letter={}
for index,user in enumerate(users):
    if 'i' in user:
        letter[user]=index

print(letter)

letter = {}
for index,user in enumerate(users):
    if user[0].lower() in ['m', 'p']:
        letter[user]=index

print(letter)
