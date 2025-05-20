from stats import count_words, character_counter, character_sorter


def main():
    num_words = count_words()
    character_count = character_counter()
    sorted_characters = character_sorter()
    print(sorted_characters)
    #print(f"{num_words} words found in the document")
    #print(character_count)

main()