from stats import num_words
from stats import char_count
from stats import sort_chars
import sys



def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def print_report(path, word_count, sorted_chars):
    report = f"""============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------"""
    
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():  
            report += f"\n{char}: {count}"
    report += "\n============= END ==============="
    
    print(report)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    full_text = get_book_text(path)
    word_count = num_words(full_text)
    character_counts = char_count(full_text)
    sorted_chars = sort_chars(character_counts)

    print_report(path, word_count, sorted_chars)

main()