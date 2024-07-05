import random
import string

def generate_password(length, use_uppercase, use_digits, use_special):
    lowercase_letters = string.ascii_lowercase
    character_pool = lowercase_letters

    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += '!@#$%^&*()_+-=[]{}|;:,.<>?'

    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice('!@#$%^&*()_+-=[]{}|;:,.<>?'))

    password.extend(random.choices(character_pool, k=length - len(password)))
    
    random.shuffle(password)

    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")

    while True:
        try:
            length = int(input("Enter the length of the password you want to generate (minimum 4): "))
            if length < 4:
                raise ValueError("Password length must be at least 4.")
            break
        except ValueError as e:
            print("Invalid input. Please enter a valid integer greater than or equal to 4.")
    
    use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
    use_special = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
    
    generated_password = generate_password(length, use_uppercase, use_digits, use_special)
    print(f"\nGenerated Password: {generated_password}")

if __name__ == "__main__":
    main()
