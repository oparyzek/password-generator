import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# enter the length of the password 
password_length = 12

new_password = generate_password(password_length)
print(f"New random password: {new_password}")