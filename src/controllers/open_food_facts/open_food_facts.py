import requests ,json,openfoodfacts
from src.controllers.database.database import Database
import datetime
def search_id(id):
    db = Database()
    cursor = db.get_cursor()
    try:
        cursor.execute("SELECT energy-kcal_100g FROM offcache WHERE id LIKE"+str(id))
        data = cursor.fetchall()
        if data != "":
            return data[0]
        else:
            fetch_id_from_api(id)
    except Exception as e:
        print(e)
        return False

def fetch_id_from_api(id):
    response_info = openfoodfacts.products.get_product(id)
    db = Database()
    cursor = db.get_cursor()


    if response_info['status'] != "0":
        cursor.execute("INSERT INTO table_name (id, name, energy-kcal_100g ) VALUES ("+str(id)+", "+response_info['product']['nutriments']['energy-kcal_100g']+", "+response_info['product']['product_name']+"); "+id)
        return int(response_info['product']['nutriments']['energy-kcal_100g'])
    else:
        return None

def search_name(name):
    print(openfoodfacts.products.search(name,1,2))

