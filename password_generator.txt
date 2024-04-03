import random
import string

def generate_password(length):
    characters = string.digits+string.ascii_letters
    password = ''.join(random.choice(characters)for i in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter the length of the password you need: "))
    password = generate_password(length)
    print("Your Password is:", password)
