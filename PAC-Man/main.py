import psycopg2
from flask import Flask, render_template, request

app = Flask(__name__)

#connect to Database
def get_db_connection():
    conn = psycopg2.connect("dbname=pacmanager user=postgres password=goodyear")
    return conn

#name and define function for each directory of website
@app.route('/')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/newvault', methods=['POST'])
 #To Do: Add case for if user already exists in Database
def newvault():
    email = request.form["email"]
    password = request.form["masterpass"]
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO pacusers (email, masterpass) VALUES (%s, %s);", (email, password))
    conn.commit()
    cur.close()
    conn.close()
    return render_template("vault.html")

@app.route('/vault', methods=['POST'])
def vault():
    email = request.form["email"]
    password = request.form["masterpass"]
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM pacusers WHERE email = %s AND masterpass = %s;", (email, password))
    valid = cur.fetchall()
    cur.close()
    conn.close()
    if valid:
        return render_template('vault.html')
    else:
       return("User not Found")

if __name__ == "__main__":
    app.run(debug=True)