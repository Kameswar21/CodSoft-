import random
import string

def password_generator():
    password_length = int(input("Enter the desired length of the password: "))

    if password_length < 8:
        print("Password length should be at least 8 characters.")
        return

    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(punctuation)
    ]

    for i in range(password_length - 4):
        password.append(random.choice(lowercase_letters + uppercase_letters + digits + punctuation))

    random.shuffle(password)

    password = ''.join(password)

    print("Generated Password : ", password)

password_generator()
