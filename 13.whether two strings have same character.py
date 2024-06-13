def count_matching_characters(str1, str2):

    if len(str1) != len(str2):
        return "The lengths of the strings are different."

    match_count = 0

    for char1, char2 in zip(str1, str2):
        
        if char1 == char2:
            match_count += 1

    return match_count

# Example usage:
string1 = "wait"
string2 = "what"
result = count_matching_characters(string1, string2)
print("Number of matching characters:", result)
