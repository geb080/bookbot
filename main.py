import sys
from stats import count_words, character_counter, character_sorter, bookbot_complete


def main():
    num_words = count_words()
    #character_count = character_counter()
    sorted_characters = character_sorter()
    finished = bookbot_complete()
    print("============ BOOKBOT ============\n")
    print(f"Analyzing book found at {sys.argv[1]}...\n")
    print("----------- Word Count ----------\n")
    print(f"Found {num_words} total words\n")
    print(f"--------- Character Count -------\n{finished}")
    print("============= END ===============")





main()