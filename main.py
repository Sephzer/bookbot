# Import necessary functions from stats.py (This goes at the top of main.py)
from stats import get_word_count, get_char_count, sort_on, get_char_list_from_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:

        print("============ BOOKBOT ============")

        book_contents = get_book_text(sys.argv[1])
        print(f"Analyzing book found at {sys.argv[1]}...")

        print("----------- Word Count ----------")
        num_words = get_word_count(book_contents)
        print(f"Found {num_words} total words")

        print("--------- Character Count -------")
        num_chars = get_char_count(book_contents)
        
        chars_from_list = get_char_list_from_dict(num_chars)
        for item in chars_from_list:
            print(f"{item['char']}: {item['num']}")
        
        print("============= END ===============")

main()