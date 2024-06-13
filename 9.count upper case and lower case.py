
upper_count = 0
lower_count = 0
while True:
    char = input("Enter a character (or '*' to end): ")
    if char == '*':
        break  
    elif char.isupper():
        upper_count += 1  
    elif char.islower():
        lower_count += 1
print("Number of uppercase characters:", upper_count)
print("Number of lowercase characters:", lower_count)
