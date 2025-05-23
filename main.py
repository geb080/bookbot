from stats import count_words, character_counter, character_sorter, bookbot_complete


def main():
    num_words = count_words()
    #character_count = character_counter()
    sorted_characters = character_sorter()
    finished = bookbot_complete()
    #print(sorted_characters)
    #print(f"{num_words} words found in the document")
    #print(character_count)
    print("============ BOOKBOT ============\n")
    print("Analyzing book found at books/frankenstein.txt...\n")
    print("----------- Word Count ----------\n")
    print(f"Found {num_words} total words\n")
    print(f"--------- Character Count -------\n{finished}")
    print("============= END ===============")





main()