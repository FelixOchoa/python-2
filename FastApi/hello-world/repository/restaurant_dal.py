from utils.restaurant import parseRestaurantToJSON
from database.connection import cursor, connection


def get_restaurant_by_document_DAL(document: str):
    try:
        query_text = f'SELECT r.id, r.name, r.email, r.phone, r.open_hour, r.closed_hour, r.description, r.avatar, r.nit FROM users u JOIN restaurants r ON u.id = r.id_user WHERE document = {document}'
        query = cursor.execute(query_text)
        query = cursor.fetchall()

        if (len(query) <= 0):
            return {
                "success": False,
                "data": []
            }
        list_restaurant = []
        for restaurant in query:
            restaurant_json = parseRestaurantToJSON(restaurant)
            list_restaurant.append(restaurant_json)

        return {
            "success": True,
            "data": list_restaurant
        }

    except Exception as e:
        return {
            "success": False,
            "message": e
        }


def get_restaurant_by_nit(nit: str):
    try:
        query_text = f'SELECT r.id, r.name, r.email, r.phone, r.open_hour, r.closed_hour, r.description, r.avatar, r.nit FROM restaurants r WHERE nit = "{nit}"'
        query = cursor.execute(query_text)
        query = cursor.fetchall()

        if (len(query) <= 0):
            return {
                "success": False,
                "data": []
            }

        if (len(query) > 0):
            restaurant_json = parseRestaurantToJSON(query[0])
            return {
                "success": True,
                "data": restaurant_json
            }

    except Exception as e:
        return {
            "success": False,
            "message": e
        }

def put_restaurant(restaurant):
    try:
        print(restaurant["nit"])
        query_text = f'UPDATE restaurants SET name = "{restaurant["name"]}", email = "{restaurant["email"]}", phone = "{restaurant["phone"]}", open_hour = "{restaurant["open_hour"]}", closed_hour = "{restaurant["closed_hour"]}", description = "{restaurant["description"]}", avatar = "{restaurant["avatar"]}" WHERE nit = "{restaurant["nit"]}"'
        print(query_text)
        query = cursor.execute(query_text)
        connection.commit()

        return {
            "success": True,
            "message": "Restaurante actualizado correctamente."
        }
    except Exception as e:
        return {
            "success": False,
            "message": e
        }

def delete_restaurant_dal(restaurant):
    try:
        query_text = f'DELETE FROM restaurants WHERE nit = "{restaurant["nit"]}"'
        query = cursor.execute(query_text)
        connection.commit()

        return {
            "success": True,
            "message": "Restaurante eliminado correctamente."
        }
    except Exception as e:
        return {
            "success": False,
            "message": e
        }
