path_to_file = "books/frankenstein.txt"

def get_word_count(file_contents):
    words = file_contents.split()
    return len(words)

def get_all_chars(file_contents):
    chars = {}

    for char in file_contents:
        char_to_lower = char.lower()

        if char_to_lower.isalpha():
            if (char_to_lower not in chars):
                chars[char_to_lower] = 1
            else:
                chars[char_to_lower] += 1

    return chars

with open(path_to_file, "r") as file:
    file_contents = file.read()
    word_count = get_word_count(file_contents)
    all_characters = get_all_chars(file_contents)

    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document\n")
    
    for char in all_characters:
        print(f"The '{char}' character was found {all_characters[char]} times")
    
    print("--- End report ---")
    
