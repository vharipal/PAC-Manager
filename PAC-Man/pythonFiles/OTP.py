import pyotp, qrcode

#For new user, creates a personalized google authenticator sign in
#Generates QR code for that user
def gen_OTP_account(email):
    key = pyotp.random_base32()
    totp = pyotp.TOTP(key) #-----> Needs to be entered into the database for each user
    uri = pyotp.totp.TOTP(key).provisioning_uri(name=email,
                                            issuer_name="Pac-Manager")
    qrcode.make(uri).save(email + ".png")

#verify that the user code is valid
def verify_OTP(passcode, totp):
    return totp.verify(passcode)

#TO DO:
#add key to database
#pull key from database to use in verify OTP function
