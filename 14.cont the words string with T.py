def count_words_with_t(input_string):
    words = input_string.split()
    count = 0
    for word in words:
        if 't' in word.lower():
            count += 1
    return count
input_string = "The quick brown fox jumps over the lazy dog"
result = count_words_with_t(input_string)
print("Number of words containing 't':", result)
