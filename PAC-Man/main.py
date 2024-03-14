from flask import Flask, render_template, request
from pythonFiles.OTP import gen_OTP_account, verify_OTP
from pythonFiles.Database import insert_to_database, verify_user

app = Flask(__name__)

#name and define function for each directory of website
@app.route('/')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/newvault', methods=['POST'])
def newvault():
#To Do: Add case for if user already exists in Database
#To Do: Verify valid email
    email = request.form["email"].lower()
    password1 = request.form["masterpass1"]
    password2 = request.form["masterpass2"]
    #check if user correctly entered password both times
    if  password1 == password2:
        insert_to_database(email, password1)
        gen_OTP_account(email)
        return render_template('vault.html')
    else: 
        return render_template("errorsignup.html")
    
'''
@app.route('/login2', methods=['POST'])
def login2():
#To Do: Add case for if user already exists in Database
#To Do: Verify valid email
    email = request.form["email"].lower()
    password1 = request.form["masterpass1"]
    password2 = request.form["masterpass2"]
    #check if user correctly entered password both times
    if  password1 == password2:
        insert_to_database(email, password1)
        gen_OTP_account(email)
        return render_template('OTP.html')
    else: 
        return render_template("errorsignup.html")

@app.route('/newervault', methods=['POST'])
def newvault():
    OTP = request.form["OTP"]
    if verify_OTP(OTP):
        return render_template("vault.html")
'''

@app.route('/vault', methods=['POST'])
def vault():
    email = request.form["email"].lower()
    password = request.form["masterpass"]
    #search databse for entry matching email/pass credential
    valid = verify_user(email, password)
    #if SQL Query finds a math valid = true
    if valid:
        return render_template("vault.html")
    else:
       return render_template("errorlogin.html")

if __name__ == "__main__":
    #turn off debug when running with host = 0.0.0.0
    #app.run(ssl_context='adhoc', host='0.0.0.0')
    app.run(debug=True)