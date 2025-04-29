import sys
from stats import get_book_word_count, get_character_count, get_sorted_dicts

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_string = get_book_text(filepath)
    word_count = get_book_word_count(book_string)
    character_count = get_character_count(book_string)
    sorted_dicts = get_sorted_dicts(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for dict in sorted_dicts:
        if not dict["char"].isalpha():
            continue
        print(f"{dict["char"]}: {dict["num"]}")
    
    print("============= END ===============")

main()