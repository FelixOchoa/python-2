import mysql.connector

connection = mysql.connector.connect(
    user="root",
    host="localhost",
    password="12345",
    database="db-restaurants",
    port="3306"
)

cursor = connection.cursor()

