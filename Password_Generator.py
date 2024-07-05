import random
import string

def generate_password(length):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    # Prompt the user to input the desired length of the password
    try:
        length = int(input("Enter the desired length for the password: "))
        if length <= 0:
            print("Please enter a positive integer.")
            return
        
        # Generate the password
        password = generate_password(length)
        
        # Display the generated password
        print("Generated Password:", password)
        
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Run the main function
if __name__ == "__main__":
    main()
