import sys
import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect("dbname=pacmanager user=postgres password=goodyear")
# Open a cursor to perform database operations
cur = conn.cursor()

def get_text(email, password):

    cur.execute("SELECT * FROM pacusers WHERE email = %s AND masterpass = %s;", (email, password))
    valid = cur.fetchall()
    if valid:
        return("User Found")
    else:
       return("User not Found")

if __name__ == "__main__":
  email = sys.argv[1]
  password = sys.argv[2]
  print(get_text(email, password))