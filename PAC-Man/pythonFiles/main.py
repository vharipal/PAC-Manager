from flask import Flask, redirect, render_template, request, session
from pythonFiles.OTP import gen_OTP_account, verify_OTP, deleteQR
from pythonFiles.Database import insert_to_database, verify_user, getTOTP, valid_email

app = Flask(__name__)

app.secret_key = 'PAC-MANAGER'

#name and define function for each directory of website
@app.route('/')
def home():
    return render_template('pachomepage.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/OTPnewuser', methods=['POST'])
def newuserOTP():
#To Do: Add case for if user already exists in Database
    email = request.form["email"].lower()
    password1 = request.form["masterpass1"]
    password2 = request.form["masterpass2"]
    #check if email is valid
    if not valid_email(email):
        return redirect('/signup')
    #check if user correctly entered password both times
    if  password1 == password2:
        insert_to_database(email, password1)
        gen_OTP_account(email)
        image = "static/" + email + ".png"
        session['image'] = image
        session['email'] = email
        return render_template('newOTP.html', image=image)
    else: 
        return render_template("errorsignup.html")

@app.route('/OTP', methods=['POST'])
def OTP():
    email = request.form["email"].lower()
    password = request.form["masterpass"]
    #search databse for entry matching email/pass credential
    valid = verify_user(email, password)
    session['email'] = email
    #if SQL Query finds a math valid = true
    if valid:
        try:
            deleteQR(email)
        except:
            pass
        return render_template("OTP.html")
    else:
       return render_template("errorlogin.html")

@app.route('/new-user-sign-in', methods=['GET', 'POST'])
def newsignin():
    image = session.get('image', None)
    email = session.get('email', None)
    totp = getTOTP(str(email)) 
    code = request.form["OTP"]

    if verify_OTP(code, totp):
        deleteQR(email)
        return redirect ('/PAC-Vault')
    else:
        return render_template('newOTP.html', image=image)
    
@app.route('/user-sign-in', methods=['POST'])
def signin():
    email = session.get('email', None)
    totp = getTOTP(str(email)) 
    code = request.form["OTP"]

    if verify_OTP(code, totp):
        return redirect('/PAC-Vault')
    else:
        return render_template('OTP.html')
    
@app.route('/PAC-Vault', methods=['GET', 'POST'])
def pVault():
    return render_template("pacuserhomepage.html")
    
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template("pacprofile.html")

if __name__ == "__main__":
    #To Do: find how to get a real SSL Cert
    #turn off debug when running with host = 0.0.0.0
    app.run(ssl_context='adhoc', host='0.0.0.0')
    #app.run(debug=True)