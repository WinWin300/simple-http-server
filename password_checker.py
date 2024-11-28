import re

# Function to check password strength
def check_password_strength(password):
    # Check if the password meets the minimum length
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    
    # Check for uppercase letter
    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one uppercase letter."
    
    # Check for lowercase letter
    if not re.search(r'[a-z]', password):
        return "Password must contain at least one lowercase letter."
    
    # Check for a number
    if not re.search(r'[0-9]', password):
        return "Password must contain at least one number."
    
    # Check for a special character
    if not re.search(r'[@$!%*?&]', password):
        return "Password must contain at least one special character (@, $, !, %, *, ?, &)."
    
    # If all conditions are met
    return "Password is strong!"

# Function to simulate password setting and validation
def set_password():
    print("Welcome to the Password Setup!")
    password = input("Please create a password: ")

    # Check if the password is strong
    result = check_password_strength(password)
    print(result)

    # If password is strong, store it (simulated here with a variable)
    if result == "Password is strong!":
        print("Your password has been set successfully!")

# Main function to run the script
def main():
    set_password()

if __name__ == "__main__":
    main()
