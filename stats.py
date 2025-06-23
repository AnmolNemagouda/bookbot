def count_words(text: str) -> int:
    """
    Counts the number of words in a given text.
    
    Args:
        text (str): The text to count words in.
        
    Returns:
        int: The number of words in the text.
    """
    return len(text.split())

def count_characters(text: str) -> int:
    """
    Counts the number of characters in a given text.
    
    Args:
        text (str): The text to count characters in.
        
    Returns:
        int: The number of characters in the text.
    """
    lower_text = text.lower()
    char_symbols_dict = {}
    for letters in lower_text:
        if letters in char_symbols_dict:
            char_symbols_dict[letters] += 1
        else:
            char_symbols_dict[letters] = 1
            
    return char_symbols_dict

def sorted_characters(text: str) -> list:
  
    char_symbols_dict = count_characters(text)
    for letters in char_symbols_dict:
        sorted_characters = sorted(
            [(char, count) for char, count in char_symbols_dict.items() if char.isalpha()],
            key=lambda item: item[1],
            reverse=True
        )
    return sorted_characters   
        
        