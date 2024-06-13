def convert_case(input_string):

    if not input_string:
        return "Empty string provided."

    conversion_type = input("Enter 'U' for uppercase, 'L' for lowercase, or 'T' for title case: ")

    if conversion_type == 'U':
        return input_string.upper() 
    elif conversion_type == 'L':
        return input_string.lower()  
    elif conversion_type == 'T':
        return input_string.title()  
    else:
        return "Invalid input. Please enter 'U', 'L', or 'T'."

# Example usage:
input_string = "Hello, World!"
converted_string = convert_case(input_string)
print("Original string:", input_string)
print("Converted string:", converted_string)
