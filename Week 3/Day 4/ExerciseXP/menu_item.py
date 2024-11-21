
# -- CREATE TABLE Menu_Items (
# -- item_id SERIAL PRIMARY KEY,
# -- item_name VARCHAR(30) NOT NULL,
# -- item_price SMALLINT DEFAULT 0
# -- )
import psycopg2
from psycopg2 import sql

class MenuItem:
    def __init__(self, item_name, item_price):
        self.item_name = item_name
        self.item_price = item_price

    def save(self):
        connection = psycopg2.connect(database = 'Restaurant',
                              user = 'postgres',
                              password = '1312',
                              host='localhost',
                              port='5432')
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO Menu_items (item_name,item_price) VALUES (%s, %s)',
            (self.item_name,self.item_price)
        )
        connection.commit()
        cursor.close()
        connection.close()

    def delete(self):
        connection = psycopg2.connect(database = 'Restaurant',
                              user = 'postgres',
                              password = '1312',
                              host='localhost',
                              port='5432')
        cursor = connection.cursor()
        cursor.execute(
            'DELETE FROM Menu_items WHERE item_name = %s',
            (self.item_name,)
        )
        connection.commit()
        cursor.close()
        connection.close()

    def update(self,new_item_name=None,new_item_price=None):
        if new_item_name:
            self.item_name = new_item_name
        if new_item_price is not None:
            self.item_price = new_item_price
        connection = psycopg2.connect(database = 'Restaurant',
                              user = 'postgres',
                              password = '1312',
                              host='localhost',
                              port='5432')
        cursor = connection.cursor()
        cursor.execute(
            'UPDATE Menu_items SET item_name = %s, item_price = %s WHERE item_name = %s',
            (self.item_name, self.item_price, self.item_name)
        )
        connection.commit()
        cursor.close()
        connection.close()

item1 = MenuItem("Ice Cream", 10)
# item1.save()

# item1.update(new_item_price=15)

item1.delete()