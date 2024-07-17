def parseRestaurantToJSON(restaurant):
    return {
        "id": restaurant[0],
        "name": restaurant[1],
        "email": restaurant[2],
        "phone": restaurant[3],
        "open_hour": restaurant[4],
        "closed_hour": restaurant[5],
        "description": restaurant[6],
        "avatar": restaurant[7],
        "nit": restaurant[8],
    }

def validateEmptyFields(restaurant):
    if restaurant.name == "" or restaurant.email == "" or restaurant.phone == "" or restaurant.open_hour == "" or restaurant.closed_hour == "" or restaurant.nit == "" or restaurant.id_user == "":
        return False
    else:
        return True