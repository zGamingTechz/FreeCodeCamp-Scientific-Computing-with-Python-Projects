def convert_to_snake_case(pascal_or_camel_cased_string):
    # Create a list of characters where uppercase characters are prefixed with '_' and converted to lowercase
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    # Join the characters into a string and strip leading '_' characters
    return ''.join(snake_cased_char_list).strip('_')

def main():
    # Example usage: Convert PascalCased string to snake_case
    print(convert_to_snake_case('IAmAPascalCasedString'))

if __name__ == '__main__':
    # Execute the main function when the script is run
    main()
