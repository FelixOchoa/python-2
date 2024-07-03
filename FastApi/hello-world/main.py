from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Restaurant(BaseModel):
    name: str
    username: str
    type: str
    address: str
    phone: str
    email: str


restaurants = [
    {
        "ID": 1,
        "name": "La Casa de Toño",
        "username": "lacasadetoño",
        "type": "Mexicana",
        "address": "Av. Insurgentes Sur 434",
        "phone": "55 1234 5678",
        "email": "lacasadetoño@example.com"
    },
    {
        "ID": 2,
        "name": "El Califa",
        "username": "elcalifa",
        "type": "Tacos",
        "address": "Av. Revolución 123",
        "phone": "55 8765 4321",
        "email": "elcalifa@example.com"
    },
]


# Create
# @app.post()

# Read

@app.get("/")
def root():
    return {"message": "Bienvenidos a mi api desarrollada con FastApi.",
            "saberMas": "https://fastapi.tiangolo.com/es/"}


@app.get("/restaurants")
def get_restaurants():
    return {
        "data": restaurants
    }


@app.get("/restaurant/{username}")
def get_restaurant(username: str):
    for restaurant in restaurants:
        if restaurant["username"] == username:
            return {
                "data": restaurant
            }
    else:
        return {
            "message": "Restaurante no encontrado."
        }


@app.post("/restaurant")
def create_restaurant(restaurant: Restaurant):
    try:
        indice = len(restaurants) + 1
        diccionario = {
            "ID": indice,
            "name": restaurant.name,
            "username": restaurant.username,
            "type": restaurant.type,
            "address": restaurant.address,
            "phone": restaurant.phone,
            "email": restaurant.email
        }

        restaurants.append(diccionario)

        return {
            "message": "Restaurante añadido correctamente.",
            "statusCode": 200,
            "infoAñadida": diccionario
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
# Update

# @app.put()
# @app.patch()

# Delete

# @app.delete()
