path_to_file = "books/frankenstein.txt"


def get_book_text(x):
    with open(x) as open_the_book:
        open_book = open_the_book.read()
    return open_book

words_to_split = get_book_text(path_to_file)

def count_words():  
    split_words = words_to_split.split()
    num_of_words = len(split_words)
    return num_of_words

def character_counter():
    character_dict = {}
    character_list = []
    for character in words_to_split:
        if character not in character_list:
            new_char = character.lower()
            character_list.append(new_char)
        else:
            continue
    
    for char in character_list:
        if char not in character_dict:
            character_dict[char]
        else:
            character_dict[char] += 1
    
    return character_dict