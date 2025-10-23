from stats import get_number_of_words, get_number_of_characters, sort_characters_by_frequency
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():

    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")

    file_path = sys.argv[1]
    
    try:
        book_text = get_book_text(file_path)
    except FileNotFoundError:
        book_text = None     
    if book_text: 
        number_of_words = get_number_of_words(book_text)
        dictionary_of_characters = get_number_of_characters(book_text)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}...")
        print("----------- Word Count ----------")
        print(f'Found {number_of_words} total words.')
        print("--------- Character Count -------")
        dictionary_of_characters = get_number_of_characters(book_text)
        sorted_characters = sort_characters_by_frequency(dictionary_of_characters)
        for char, count in sorted_characters.items():
            print(f"{char}: {count}")
    else:
        print("Error: No book text found.")

    

main()