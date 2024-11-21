import psycopg2
import requests
import json
import random

connection = psycopg2.connect(database = 'countries',
                              user = 'postgres',
                              password = '1312',
                              host='localhost',
                              port='5432')

cursor = connection.cursor()
cursor.execute('DROP TABLE IF EXISTS random_countries')
create_table_query = '''
    CREATE TABLE random_countries (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        capital VARCHAR(100) NOT NULL,
        flag_code VARCHAR(100),
        population INTEGER,
        subregion VARCHAR(100) NOT NULL
    );
'''
cursor.execute(create_table_query)
connection.commit()

countries_api = requests.get('https://restcountries.com/v3.1/all')
data = countries_api.json()
print(data[0]) # IMPORTANT CHECK THE TYPE OF DATA YOU WILL GET FROM THE API

for i in range(10):
    index = random.randint(1, 100)
    try:
        name = data[index]['name']['official']
    except:
        name = data[index]['name']['official'][0]
        
    name = name.replace('\'','`')
    capital = data[index]['capital'][0]
    flag_code = data[index]['flag']
    population = data[index]['population']
    subregion = data[index]['subregion']

    query = f'''INSERT INTO random_countries (name, capital, flag_code, population, subregion)
    VALUES ('{name}', '{capital}', '{flag_code}', '{population}', '{subregion}')'''
    cursor.execute(query)
    connection.commit()
    
connection.close()
print('Successfully added')
