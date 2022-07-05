import openfoodfacts
from src.controllers.database.database import Database


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
        cursor.execute("INSERT INTO table_name (id, name, energy-kcal_100g ) VALUES ("+str(id)+", "+response_info['product']['nutriments']['energy-kcal_100g']+", "+response_info['product']['product_name']+"); ")
        return int(response_info['product']['nutriments']['energy-kcal_100g'])
    else:
        return None


def search_name(name):
    db = Database()
    cursor = db.get_cursor()
    results = openfoodfacts.products.search(name, 0, 10)
    for key in results["products"]:
        code = str(key['code'])
        if 'energy-kcal_100g' in key['nutriments']:
            if key['nutriments']['energy-kcal_100g']!='':
                kcal = str(key['nutriments']['energy-kcal_100g'])
                if 'product_name_de' in key:
                    if key['product_name_de'].isalnum() & len(key['product_name_de']) > 0:
                        product_name = key['product_name_de']
                        cursor.execute("INSERT IGNORE INTO food (FoodID, Name, Calories ) VALUES (%s, %s, %s)",(code,product_name,kcal))
                    else:
                        product_name = key['product_name_de']
                        cursor.execute("INSERT IGNORE INTO food (FoodID, Name, Calories ) VALUES (%s, %s, %s)",(code,product_name,kcal))
                else:
                    cursor.execute("INSERT IGNORE INTO food (FoodID, Name, Calories ) VALUES (%s, %s, %s)",(code,product_name,kcal))
    return results


def add_food(food_id,food_amount,user):
    db = Database()
    cursor = db.get_cursor()
    date = datetime.datetime.now().date().strftime("%Y-%m-%d")
    cursor.execute("SELECT CaloriesID FROM calories WHERE Date LIKE %s AND UserID LIKE %s ",( date, user.get_id()))
    i=cursor.fetchall()
    print(i)
    calories_id = i[0]
    cursor.execute("INSERT INTO food_track (CaloriesID,FoodID, Count ) VALUES (%s, %s, %s)",(calories_id,food_id,food_amount))
