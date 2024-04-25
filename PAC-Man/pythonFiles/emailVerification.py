from flask import Flask, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import uuid

app = Flask(__name__)

# Temporary storage for verification tokens
verification_tokens = {}

def send_verification_email(email):
    sender_email = "pacmanagerauthentication@gmail.com" #sender email
    sender_password = "rEZ)8_*zG}I+@215J^yH" #sender password
    
    # Generate a unique token using UUID
    token = str(uuid.uuid4())

    verification_link = f"http://yourserver.com/verify_email?token={token}" #Needs to be fixed with actual server still, I just don't know it

    # Email content
    subject = "Verify Your Email Address"
    body = f"Please click the following link to verify your email address: {verification_link}"
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Connect to SMTP server and send email
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender_email, sender_password)
        text = message.as_string()
        server.sendmail(sender_email, email, text)
        server.quit()
        print("Verification email sent successfully.")
        # Store the token temporarily for verification
        verification_tokens[token] = email
    except Exception as e:
        print("Error sending email:", str(e))

@app.route('/verifyEmail', methods=['GET'])
def verifyEmail():
    # Extract the token from the query parameters
    token = request.args.get('token')
    
    # Check if the token exists in the verification_tokens dictionary
    if token in verification_tokens:
        # Token exists
        email = verification_tokens[token]  # Get the email associated with the token
        del verification_tokens[token]  # Remove the token from storage
        emailVerified = True
        
        # Return a success response
        return emailVerified
    else:
        # Invalid or expired token
        emailVerified = False
        return emailVerified

if __name__ == '__main__':
    app.run(debug=True)
