from fastapi import FastAPI
from pydantic import BaseModel
from database.connection import cursor, connection
from utils.restaurant import parseRestaurantToJSON, validateEmptyFields
from repository.restaurant_dal import get_restaurant_by_document_DAL, get_restaurant_by_nit, put_restaurant, delete_restaurant_dal
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
        if (document == ""):
            return {
                "message": "No se puede enviar campos vacíos.",
                "statusCode": 400
            }

        result = get_restaurant_by_document_DAL(document)

        if (result["success"] == False):
            return {
                "message": "No se encontró información de los restaurantes asociados a este usuario.",
                "statusCode": 404
            }

        if (result["success"] == True):
            return {
                "data": result["data"],
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


@app.put("/restaurant/{nit}")
def update_restaurant_put(nit: str, restaurant: Restaurant):
    try:
        if (nit == ""):
            return {
                "message": "No se puede enviar campos vacíos.",
                "statusCode": 400
            }

        result = get_restaurant_by_nit(nit)

        if (result["success"] == False):
            return {
                "message": "No se encontró información relacionada a un restaurante.",
                "statusCode": 404
            }

        restaurant_copy = {
            "name": restaurant.name,
            "email": restaurant.email,
            "phone": restaurant.phone,
            "open_hour": restaurant.open_hour,
            "closed_hour": restaurant.closed_hour,
            "description": restaurant.description,
            "avatar": restaurant.avatar,
            "nit": restaurant.nit,
        }

        result_put = put_restaurant(restaurant_copy)

        if (result_put["success"] == False):
            return {
                "message": result_put["message"],
                "statusCode": 500
            }

        return {
            "message": result_put["message"],
            "statusCode": 200
        }

    except Exception as e:
        return {
            "message": f"Ocurrió el siguiente error: {e}",
            "statusCode": 500
        }


@app.patch("/restaurant/{username}")
def update_restaurant_patch(username: str, fields: dict):
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


@app.delete("/restaurant/{nit}")
def delete_restaurant(nit: str):
    try:
        if (nit == ""):
            return {
                "message": "No se puede enviar campos vacíos.",
                "statusCode": 400
            }

        result = get_restaurant_by_nit(nit)

        if (result["success"] == False):
            return {
                "message": "No se encontró información relacionada a un restaurante.",
                "statusCode": 404
            }

        result_delete = delete_restaurant_dal(result["data"])

        if (result_delete["success"] == False):
            return {
                "message": result_delete["message"],
                "statusCode": 500
            }

        return {
            "message": result_delete["message"],
            "statusCode": 200
        }

    except Exception as e:
        return {
            "message": f"Ocurrió el siguiente error: {e}",
            "statusCode": 500
        }
