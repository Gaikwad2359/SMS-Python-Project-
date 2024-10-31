from pymongo import MongoClient
import mysql.connector

# MongoDB Configuration
client = MongoClient("mongodb://localhost:27017/")
db = client["sms_management"]
config_collection = db["config"]

# MySQL Configuration
mysql_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="sms_metrics"
)
mysql_cursor = mysql_connection.cursor()
