from stats import count_words
from stats import character_counter

def main():
    num_words = count_words()
    character_count = character_counter()
    print(f"{num_words} words found in the document")
    print(character_count)

main()