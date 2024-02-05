def verify_card_number(card_number):
    # Initialize the sum of odd digits
    sum_of_odd_digits = 0
    
    # Reverse the card number for easier iteration
    card_number_reversed = card_number[::-1]
    
    # Extract odd digits from reversed card number
    odd_digits = card_number_reversed[::2]

    # Sum the odd digits
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    # Initialize the sum of even digits
    sum_of_even_digits = 0
    
    # Extract even digits from reversed card number
    even_digits = card_number_reversed[1::2]
    
    # Sum the even digits after doubling and adjusting for digits greater than 9
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    
    # Calculate the total sum of odd and even digits
    total = sum_of_odd_digits + sum_of_even_digits
    
    # Output the total sum for debugging purposes
    print(total)
    
    # Check if the total sum is divisible by 10 to verify card validity
    return total % 10 == 0

def main():
    # Example card number with spaces and dashes
    card_number = '4111-1111-4555-1141'
    
    # Remove spaces and dashes from the card number
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    # Check and print the validity of the card number
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

# Execute the main function
main()
