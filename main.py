from stats import get_num_words, get_character_counts, get_sorted_counts
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        contents = file.read()
    return contents

def generate_report(book_path, num_words, dictionary):

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in dictionary.items():
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    contents = get_book_text(book_path)    
    num_words = get_num_words(contents)
    char_counts = get_character_counts(contents)
    sorted_dict = get_sorted_counts(char_counts)
    
    generate_report(book_path, num_words, sorted_dict)

main()