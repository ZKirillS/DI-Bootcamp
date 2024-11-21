import psycopg2
from menu_item import MenuItem

class MenuManager:
    @classmethod
    def get_by_name(cls,name):
        connection = psycopg2.connect(database = 'Restaurant',
                              user = 'postgres',
                              password = '1312',
                              host='localhost',
                              port='5432')
         
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM Menu_Items WHERE item_name = %s", (name,)
        )
        result = cursor.fetchone()
        cursor.close()
        connection.close()

        if result:
            return MenuItem(result[1], result[2])
        return None

    @classmethod
    def all_items(self):
        connection = psycopg2.connect(database = 'Restaurant',
                              user = 'postgres',
                              password = '1312',
                              host='localhost',
                              port='5432')
         
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM Menu_Items"
        )
        result = cursor.fetchall()
        cursor.close()
        connection.close()

        items = []
        for row in result:
            items.append(MenuItem(row[1],row[2]))
        return items
    
