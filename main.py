from stats import count_words, count_characters, sorted_characters
import sys 

def get_book_text(file_path: str) -> str:
    """
    Reads the content of a book file and returns it as a string.
    
    Args:
        file_path (str): The path to the book file.
        
   Write a main function that uses get_book_text with the relative path to your frankenstein.txt file to print the entire contents of the book to the console.
    """
    
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
        return file_content
    
def main():
    """
    Main function to execute the book reading functionality.
    """
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:    
        book_text = get_book_text(sys.argv[1])
        num_words = count_words(book_text)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        sorted_chars = sorted_characters(book_text)
        for char, num in sorted_chars:
            print(f"{char}: {num}")
    
    
main()