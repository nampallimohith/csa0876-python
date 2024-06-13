def process_string(input_string):
    uppercase_string = input_string.upper()
    space_count = input_string.count(' ')
    return uppercase_string, space_count
input_string = "Python is the interpreted language"
uppercase_string, space_count = process_string(input_string)
print(f"Uppercase String: {uppercase_string}")
print(f"Number of spaces: {space_count}")
