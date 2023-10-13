def octal_to_decimal_with_decimal_places(octal_int, decimal_places):
    # Convert the octal integer to an octal string
    octal_str = str(octal_int)

    # Separate the integer and fractional parts using the decimal point
    if '.' in octal_str:
        integer_part_str, fractional_part_str = octal_str.split('.')
    else:
        integer_part_str, fractional_part_str = octal_str, ''

    # Convert the integer part to decimal
    decimal_integer = 0
    position = len(integer_part_str) - 1
    for digit in integer_part_str:
        decimal_integer += int(digit) * (8 ** position)

    # Convert the fractional part to decimal
    decimal_fractional = 0
    position = -1
    for digit in fractional_part_str:
        decimal_fractional += int(digit) * (8 ** position)
        position -= 1

    # Combine the integer and fractional parts to get the decimal number
    decimal_num = decimal_integer + decimal_fractional

    # Round the decimal number to the specified number of decimal places
    decimal_num = round(decimal_num, decimal_places)

    return decimal_num

# Example usage:
octal_int = 124123.123123  # Replace with your octal number as an integer
decimal_places = 2  # Replace with the desired number of decimal places
decimal_num = octal_to_decimal_with_decimal_places(octal_int, decimal_places)
print(decimal_num)

