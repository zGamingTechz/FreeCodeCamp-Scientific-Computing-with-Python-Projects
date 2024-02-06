import re
import secrets
import string

def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    """
    Generate a password with specified constraints.

    Parameters:
    - length (int): Length of the password (default is 16).
    - nums (int): Minimum number of digits in the password (default is 1).
    - special_chars (int): Minimum number of special characters in the password (default is 1).
    - uppercase (int): Minimum number of uppercase letters in the password (default is 1).
    - lowercase (int): Minimum number of lowercase letters in the password (default is 1).

    Returns:
    - str: Generated password.
    """
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        constraints = [
            (nums, r'\d'),                            # Constraint for digits
            (special_chars, fr'[{symbols}]'),         # Constraint for special characters
            (uppercase, r'[A-Z]'),                    # Constraint for uppercase letters
            (lowercase, r'[a-z]')                      # Constraint for lowercase letters
        ]

        # Check constraints
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    
    return password

if __name__ == '__main__':
    # Example usage: Generate a password with default constraints
    new_password = generate_password()
    print('Generated password:', new_password)
