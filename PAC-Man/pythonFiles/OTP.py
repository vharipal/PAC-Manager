import pyotp, qrcode, os

#For new user, creates a personalized google authenticator sign in
#Generates QR code for that user
def gen_OTP_account(email):
    key = pyotp.random_base32()
    totp = pyotp.TOTP(key) #-----> Needs to be entered into the database for each user
    uri = pyotp.totp.TOTP(key).provisioning_uri(name=email,
                                            issuer_name="Pac-Manager")
    code = email + ".png"
    qrcode.make(uri).save(code)
    moveCode(code)

#verify that the user code is valid
def verify_OTP(passcode, totp):
    return totp.verify(passcode)

def moveCode(code):
    os.system("mv " + code + " /static")

#TO DO:
#add key to database
#pull key from database to use in verify OTP function
