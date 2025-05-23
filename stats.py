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
    #using a list so i can make everything lowercase and store the values temporarily as strings
    character_dict = {}
    character_list = []
    
    #loop over words to split (which is already in str format)
    for character in words_to_split:
        #add characters to list
        new_char = character.lower()
        character_list.append(new_char)
        
    
    #loop over list to add characters as keys to dictionary and assign values to those keys
    for char in character_list:

        if char not in character_dict:
            character_dict[char] = 1
        else:
            character_dict[char] += 1
    
    return character_dict

characters_to_sort = character_counter()

def get_val(x):
    val_list = []
    for value in characters_to_sort:
        character_values = characters_to_sort[value]
        val_list.append(character_values)
    return val_list[x]

for value in characters_to_sort:
    character_values = characters_to_sort[value]

def sort_on(dict):
    return dict["num"]

def character_sorter():
    ultimate_list = []
    count = 0
    for char in characters_to_sort:
        char_dict = {}
        char_dict["char"] = char
        value = get_val(count)
        count += 1
        char_dict["num"] = value
        ultimate_list.append(char_dict)

    ultimate_list.sort(reverse=True, key=sort_on)
   

    return ultimate_list

   

final_form = character_sorter()



def bookbot_complete():
    srsly_last = ""
    last_list = []
    for value in final_form:
        final_dict = value
        character = final_dict['char']
        val = final_dict['num']
        if character.isalpha() == True:
            last_list.append(f"{character}: {val}")
        else:
            continue
    
    for val in last_list:
        new_val = val+"\n"
        srsly_last += new_val
    
    return srsly_last

