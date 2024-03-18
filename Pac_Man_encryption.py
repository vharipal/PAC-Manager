from Crypto.Cipher import AES
from argon2 import PasswordHasher
from pbkdf2 import PBKDF2
from base64 import b64encode, b64decode
import os


def generate_salt():
    #Generate a random 32byte value for each user
    return os.urandom(32)

def hash_master_password(master_password, salt):
    # Create an Argon2 password hasher
    ph = PasswordHasher()

    # Hash the master password with Argon2
    hashed_password = ph.hash(master_password.encode() + salt)
    return hashed_password



def encrypt_password(password_to_encrypt, hashed_master_password, user_salt):
    key = PBKDF2(hashed_master_password, user_salt).read(32) #Derives a key from hashed master master password and unique salt

    data_convert = password_to_encrypt.encode('utf-8') 

    cipher = AES.new(key, AES.MODE_EAX) #create AES cipher object

    ciphertext = cipher.encrypt_and_digest(data_convert) #encrpytion of pasword 

    encoded_ciphertext = b64encode(user_salt + cipher.nonce + ciphertext).decode()

    return encoded_ciphertext

def decrypt_password(password_to_decrypt, hashed_master_password):

    convert = b64decode(password_to_decrypt)#decode stored password

    user_salt = convert[:32]
    nonce = convert[32:48]
    ciphertext = convert[48:]

    key = PBKDF2(hashed_master_password, user_salt).read(32)#Derives a key from hashed master master password and unique salt

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

    plaintext = cipher.decrypt(ciphertext)

    return plaintext

#usersalt = generate_salt()
#hsp=hash_master_password("goodyear",usersalt)
#epsswd= encrypt_password("goodyear1",hsp,usersalt)
#print(decrypt_password(epsswd,hsp))

