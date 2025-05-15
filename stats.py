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
    #establishes our list and the dictionary that it will be converted to.
    #its in list form so i can make everything lowercase and store the values temporarily as strings
    character_dict = {}
    character_list = []
    #loop over words to split (which is already in str format)
    for character in words_to_split:
        #add characters to list
        if character not in character_list:
            new_char = character.lower()
            character_list.append(new_char)
        else:
            continue
    
    #loop over list to add characters as keys to dictionary and assign values to those keys
    for char in character_list:
        
        if char not in character_dict:
            character_dict[char] = 1
        else:
            character_dict[char] += 1

    return character_dict