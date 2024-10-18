import random
import string

# Function to generate password
def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""
    
    if use_letters:
        characters += string.ascii_letters  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if use_numbers:
        characters += string.digits  # '0123456789'
    if use_symbols:
        characters += string.punctuation  # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    
    if not characters:
        print("Error: No character sets selected. Please select at least one option.")
        return None
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Function to prompt user for password preferences
def password_generator():
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Password length must be a positive number.")
            return
        
        print("\nSelect the character types for the password:")
        use_letters = input("Include letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
        
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        
        if password:
            print(f"\nGenerated Password: {password}")
    except ValueError:
        print("Please enter a valid number for the password length.")

# Run the password generator
password_generator()
