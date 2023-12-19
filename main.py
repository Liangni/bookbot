def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = get_num_words(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    char_dict = get_chars_dict(text)
    sorted_chars_list = chars_dict_to_sorted_list(char_dict)
    for item in sorted_chars_list:
        print(f"The {item['char']} character was found {item['num']} times")

    print("--- End report ---")

def get_num_words(text):
    word_list = text.split()
    return len(word_list)

def get_book_text(path):
    with open(path) as file:
        return file.read()

def get_chars_dict(text):
    chars = {}

    for char in text:
        lowercase_char = char.lower()
        if not (lowercase_char.isalpha()):
            continue

        if lowercase_char in chars:
            chars[lowercase_char] += 1
        else:
            chars[lowercase_char] = 1
    return chars

def sort_on(dictionary):
    return dictionary["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({ "char": ch, "num": num_chars_dict[ch]})   
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()