import secrets
import string

from numpy import character

def password_generator(password_length):
    characters=string.ascii_letters+string.digits

    secure_password=''.join(secrets.choice(characters) for i in range(password_length))
    return secure_password

def main():
    user_password_length=int(input("Input number of digits for password: "))
    print("Password generated: ", password_generator(user_password_length))

main()
