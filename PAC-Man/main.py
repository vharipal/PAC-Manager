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
#To Do: Verify valid email
def newvault():
    email = request.form["email"].lower()
    password1 = request.form["masterpass1"]
    password2 = request.form["masterpass2"]
    conn = get_db_connection()
    cur = conn.cursor()
    #check if user correctly entered password both times
    if  password1 == password2:
        cur.execute("INSERT INTO pacusers (email, masterpass) VALUES (%s, %s);", (email, password2))
        conn.commit()
        cur.close()
        conn.close()
        return render_template("vault.html")
    else: 
        cur.close()
        conn.close()
        return render_template("errorsignup.html")

@app.route('/vault', methods=['POST'])
def vault():
    email = request.form["email"].lower()
    password = request.form["masterpass"]
    conn = get_db_connection()
    cur = conn.cursor()
    #search databse for entry matching email/pass credential
    cur.execute("SELECT * FROM pacusers WHERE email = %s AND masterpass = %s;", (email, password))
    valid = cur.fetchall()
    cur.close()
    conn.close()
    #if SQL Query finds a math valid = true
    if valid:
        return render_template("vault.html")
    else:
       return render_template("errorlogin.html")

if __name__ == "__main__":
    #turn off debug when running with host = 0.0.0.0
    app.run(debug=True, ssl_context='adhoc', host='0.0.0.0')