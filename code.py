import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""
    
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected.")
    
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    print("Welcome to the Random Password Generator")

    try:
        length = int(input("Enter the desired password length: "))
        
        use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

        if length <= 0:
            print("Please enter a positive integer for length.")
            return
        
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Generated Password: {password}")

    except ValueError:
        print("Please enter a valid number for the length.")

if __name__ == "__main__":
    main()
