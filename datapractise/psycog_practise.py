# Small script to show PostgreSQL and Pyscopg together
import psycopg2

conn = psycopg2.connect("dbname='XYZ user='postgres' host='localhost' password='XYZ!'")

try:
   if conn:
    print("Logged in")
except:
    print("I am unable to connect to the database")