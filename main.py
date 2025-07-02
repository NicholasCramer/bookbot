from stats import get_word_count, get_character_count, sort_dict, strip_non_alpha_from_dict
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        book_text = f.read()
    return book_text

def main():
    line_args = sys.argv
    if len(line_args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    text = get_book_text(line_args[1])
    num_words = get_word_count(text)
    num_chars = get_character_count(text)
    alpha_dict = strip_non_alpha_from_dict(num_chars)
    sorted_dictionary = sort_dict(alpha_dict)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {line_args[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for k, v in sorted_dictionary.items():
        print(f"{k}:", f"{v}")
    print("============= END ===============")
    
main()