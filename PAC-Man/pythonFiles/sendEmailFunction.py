import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendEmail(email):

    #Sender email info
    senderEmail = 'pacmanagerauthentication@gmail.com' #Email address
    senderPass = 'rEZ)8_*zG}I+@215J^yH' #Email Password

    #Email Contents
    subject = "Pac-Manager Email Verification"
    body = "Please click the following link to verify your email address: <verification_link>"
    message = MIMEMultipart()
    message["From"] = senderEmail
    message["To"] = email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    #SMTP server connection
    try:
        server = smtplib.SMTP("smtp.gmail.com", 465)
        server.starttls()
        server.login(senderEmail, senderPass)
        text = message.as_string()
        server.sendmail(senderEmail, email, text)
        server.quit()
        print("Verification email sent successfully.")
    except Exception as e:
        print("Error sending email:", str(e))