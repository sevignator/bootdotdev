def main():
    book_path = './books/frankeinstein.txt'
    file_contents = get_book_text(book_path)
    word_count = get_word_count(file_contents)
    char_count = get_char_dict(file_contents)
    print_report(word_count, char_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_dict(text):
    chars = {}

    for char in text:
        sanitized_char = char.lower()

        if not sanitized_char.isalpha():
            continue

        if sanitized_char not in chars:
            chars[sanitized_char] = 1
            continue

        chars[sanitized_char] += 1

    return chars

def print_report(word_count, char_dict):
    chars_list = list(char_dict.items())
    chars_list.sort(key=(lambda x : x[1]), reverse=True)

    print('--- Begin report of books/frankenstein.txt ---')
    print(f"{word_count} words found in the document")
    print('')

    for char in chars_list:
        print(f"The '{char[0]}' character was found {char[1]} times")

    print('--- End report ---')

main()
