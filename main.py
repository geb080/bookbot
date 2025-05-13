path_to_file = "books/frankenstein.txt"


def main():
    num_words = count_words()
    print(f"{num_words} words found in the document")


def get_book_text(x):
    with open(x) as open_the_book:
        open_book = open_the_book.read()
    return open_book

def count_words():
    words_to_split = get_book_text(path_to_file)
    split_words = words_to_split.split()
    num_of_words = len(split_words)
    return num_of_words


#count_words()
main()