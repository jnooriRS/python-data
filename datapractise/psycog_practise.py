# Small script to show PostgreSQL and Pyscopg together
import psycopg2
import psycopg2.extras

connection_to_db = psycopg2.connect("dbname='XYZ' user='postgres' host='localhost' password='XYZ'")

try:
   if connection_to_db:
    print("Logged in")
except:
    print("I am unable to connect to the database")


cur = connection_to_db.cursor()
cur.execute(    "SELECT * from weather "    )
rows = cur.fetchall()
print ("\nShow me the databases:\n")
for row in rows:
    print("   ", row[0])

#Good tutorial to follow