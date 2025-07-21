# password_generator.py

import string
import random

def generate_password(length=12, use_digits=True, use_special=True):
    """
    Generates a secure random password.
    
    Parameters:
    - length: int, length of the password
    - use_digits: bool, include digits
    - use_special: bool, include punctuation characters
    
    Returns:
    - str: generated password
    """
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    return ''.join(random.choice(characters) for _ in range(length))

def main():
    print("🔐 Welcome to the Password Generator!")
    try:
        length = int(input("Enter desired password length: "))
        digits_choice = input("Include digits? (y/n): ").lower() == 'y'
        special_choice = input("Include special characters? (y/n): ").lower() == 'y'

        password = generate_password(length, digits_choice, special_choice)
        print(f"\n✅ Your generated password is:\n{password}")

    except ValueError:
        print("❌ Invalid input. Please enter a valid number for length.")

if __name__ == "__main__":
    main()
