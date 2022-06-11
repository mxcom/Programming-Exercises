import requests ,json
from src.controllers.database.database import Database
import datetime
def search_id(id):
    db = Database()
    cursor = db.get_cursor()
    try:
        cursor.execute("SELECT energy-kcal_100g FROM offcache WHERE id LIKE"+id)
        data = cursor.fetchall()
        if data != "":
            return data[0]
        else:
            fetch_id_from_api(id)
    except Exception as e:
        print(e)
        return False

def fetch_id_from_api(id):
    response = requests.get('https://world.openfoodfacts.org/api/v0/product/'+id).text
    response_info = json.loads(response)
    db = Database()
    cursor = db.get_cursor()
    if response_info['status'] != "0":
        cursor.execute("INSERT INTO table_name (id, name, energy-kcal_100g ) VALUES ("+id+", "+int(response_info['product']['nutriments']['energy-kcal_100g'])+", "+int(response_info['product']['product_name'])+"); "+id)
        return int(response_info['product']['nutriments']['energy-kcal_100g'])
    else:
        return None
