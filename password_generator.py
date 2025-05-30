import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    # Create a combination of all types of characters
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly pick characters
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired length of the password: "))
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()



