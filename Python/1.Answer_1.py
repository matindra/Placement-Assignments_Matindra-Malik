def highest_frequency(input_string):
    words = input_string.split()

    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    max_frequency = 0
    for count in word_counts.values():
        if count > max_frequency:
            max_frequency = count

    highest_frequency_word_length = 0
    for word, count in word_counts.items():
        if count == max_frequency and len(word) > highest_frequency_word_length:
            highest_frequency_word_length = len(word)

    return highest_frequency_word_length


# test case 1

string = "python java python java python java python"
result = highest_frequency(string)
print(result)

# Explaination: In this case, the word "python" appears four times, which is the highest frequency.
# Its length is 6 characters, so the program returns 6.

# test case 2
string = "data science machine learning data anayst data"
result = highest_frequency(string)
print(result)

# Explaination: In this case, the word "data" appears three times, which is the highest frequency.
# Its length is 4 characters, so the program returns 4.