from fastapi import FastAPI
from pydantic import BaseModel
from database.connection import cursor, connection
from utils.restaurant import parseRestaurantToJSON, validateEmptyFields
import time
app = FastAPI()

restaurants = []


class Restaurant(BaseModel):
    name: str
    email: str
    phone: str
    open_hour: str
    closed_hour: str
    description: str
    avatar: str
    nit: str
    id_user: int


@app.get("/")
def root():
    return {"message": "Bienvenidos a mi api desarrollada con FastApi.",
            "saberMas": "https://fastapi.tiangolo.com/es/"}


@app.get("/restaurants")
def get_restaurants():
    query = cursor.execute("SELECT * FROM restaurants")
    query = cursor.fetchall()

    for restaurant in query:
        if (restaurant and len(query) > 0):
            restaurant_json = parseRestaurantToJSON(restaurant)
            restaurants.append(restaurant_json)

    return {
        "data": restaurants
    }


@app.get("/restaurant-by-user-document/{document}")
def get_restaurant_by_user_document(document: str):
    try:
        query_text = f'SELECT r.id, r.name, r.email, r.phone, r.open_hour, r.closed_hour, r.description, r.avatar, r.nit FROM users u JOIN restaurants r ON u.id = r.id_user WHERE document = {document}'
        query = cursor.execute(query_text)
        query = cursor.fetchall()

        if (len(query) <= 0):
            return {
                "message": "No se encontró información de los restaurantes asociados a este usuario.",
                "statusCode": 404
            }

        list_restaurant = []
        for restaurant in query:
            restaurant_json = parseRestaurantToJSON(restaurant)
            list_restaurant.append(restaurant_json)

        return {
            "data": list_restaurant,
            "statusCode": 200
        }
    except Exception as e:
        return {
            "message": f"Ocurrió el siguiente error: {e}",
            "statusCode": 500
        }


@app.post("/restaurant")
def create_restaurant(restaurant: Restaurant):
    try:
        if (validateEmptyFields(restaurant)):
            query_text = f'INSERT INTO restaurants (name, email, phone, open_hour, closed_hour, description, avatar, nit, id_user) VALUES ("{restaurant.name}", "{restaurant.email}", "{restaurant.phone}", "{restaurant.open_hour}", "{restaurant.closed_hour}", "{restaurant.description}", "{restaurant.avatar}", "{restaurant.nit}", "{restaurant.id_user}")'
            query = cursor.execute(query_text)
            connection.commit()
        else:
            return {
                "message": "Todos los campos son obligatorios.",
                "statusCode": 400
            }

        return {
            "message": "Restaurante añadido correctamente.",
            "statusCode": 200,
        }

    except Exception as e:
        return {
            "message": f"Ocurrió el siguiente error: {e}",
            "statusCode": 500
        }


@app.patch("/restaurant/{username}")
def update_restaurant_patch(username: str, restaurant: Restaurant):
    try:
        for i in range(len(restaurants)):
            if restaurants[i]["username"] == username:
                nuevoRestaurant = {
                    "ID": restaurants[i]["ID"],
                    "name": restaurant.name,
                    "username": restaurant.username,
                    "type": restaurant.type,
                    "address": restaurant.address,
                    "phone": restaurant.phone,
                    "email": restaurant.email
                }
                restaurants[i] = nuevoRestaurant
                return {
                    "message": "Restaurante actualizado correctamente.",
                    "statusCode": 200,
                    "infoActualizada": nuevoRestaurant,
                }
        else:
            return {
                "message": "Restaurante no encontrado.",
                "statusCode": 404
            }
    except Exception as e:
        return {
            "message": f"Ocurrió el siguiente error: {e}",
            "statusCode": 500
        }


@app.put("/restaurant/{username}")
def update_restaurant_put(username: str, fields: dict):
    try:
        for i in range(len(restaurants)):
            if restaurants[i]["username"] == username:
                if len(fields) == 0:
                    return {
                        "message": "No se proporcionaron campos para actualizar.",
                        "statusCode": 400
                    }
                else:
                    for key, value in fields.items():
                        if (restaurants[i][key] != ""):
                            restaurants[i][key] = value
                        else:
                            return {
                                "message": f"El campo {key} no es válido.",
                                "statusCode": 400
                            }
                    return {
                        "message": "Restaurante actualizado correctamente.",
                        "statusCode": 200,
                        "infoActualizada": restaurants[i]
                    }
        else:
            return {
                "message": "Restaurante no encontrado.",
                "statusCode": 404
            }
    except Exception as e:
        return {
            "message": f"Ocurrió el siguiente error: {e}",
            "statusCode": 500
        }


@app.delete("/restaurant/{username}")
def delete_restaurant(username: str):
    try:
        for i in range(len(restaurants)):
            if restaurants[i]["username"] == username:
                restaurants.pop(i)
                return {
                    "message": "Restaurante eliminado correctamente.",
                    "statusCode": 200
                }
        else:
            return {
                "message": "Restaurante no encontrado.",
                "statusCode": 404
            }
    except Exception as e:
        return {
            "message": f"Ocurrió el siguiente error: {e}",
            "statusCode": 500
        }