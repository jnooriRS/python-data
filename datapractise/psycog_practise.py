# Small script to show PostgreSQL and Pyscopg together
import psycopg2
import psycopg2.extras

connection_to_db = psycopg2.connect("dbname='anthony_training' user='postgres' host='localhost' password='Rowing31!'")

try:
   if connection_to_db:
    print("Logged in")
except:
    print("I am unable to connect to the database")


cur = conn.cursor()
cur.execute("SELECT ** FROM weather ")

#Good tutorial to follow