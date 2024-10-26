# Accessing book file 
def main():
    with open('books/frankenstein.txt') as f:

        file_contents = f.read()
    return file_contents

# Counting words 
def count_words(text):

    words = text.split()
    return len(words)

# Counting characters
def count_characters(text): 
    # Empty dictionary to store character counts 
    char_count = {}

    # Converts text to lowercase and loops over each character 
    for char in text.lower():
        # Counting alphabet only 
        if char.isalpha(): 
            if char in char_count: 
                char_count[char] += 1 
            else: 
                char_count[char] = 1 

    return char_count

def print_report(file_path, word_count, char_count): 
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")

    # Sorting characters by frequency, from most to least common
    sorted_char_count = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    for char, count in sorted_char_count: 
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

# Calling main() to get file contents
file_contents = main()

# Get word and character counts 
word_count = count_words(file_contents)
char_count = count_characters(file_contents)

# Print report 
print_report('books/frankenstein.txt', word_count, char_count)