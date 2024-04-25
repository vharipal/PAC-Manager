from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def password_check(password):
    strength = 0 

    if len(password) > 8: #makes sure password is atleast of length 8
        strength +=1 
    
    if  re.search(r'[A-Z]', password): #checks to see if password contains atleast 1 capital letter
        strength +=1 
    
    if  re.search(r'[a-z]', password): #checks to see if pasword contains atleast 1 lowercase letter 
        strength +=1 
    
    if  re.search(r'\d', password): #checks to see if password contains atleast 1 digit
        strength +=1 
    
    if any(not c.isalnum() for c in password): #checks to see if passwrod contains atleast 1 special character 
        strength +=1 
    
    return strength


def password_print(strength):
    if strength == 5:
        print("Password is very strong!")
    elif strength >= 3:
        print("Password is strong.")
    elif strength >= 2:
        print("Password is moderate.")
    elif strength >= 1:
        print("Password is weak.")
    else:
        print("Password is very weak.")


@app.route('/password_check', methods=['POST'])
def check_password():
    data = request.get_json()
    password = data.get('password')
    strength = password_check(password)
    return jsonify({"strength": strength})