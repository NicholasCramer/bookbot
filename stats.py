def get_word_count(book_text):
    word_count = len(book_text.split())
    return word_count

def get_character_count(book_text):
    char_dict = {}
    for c in book_text.lower():
        char_dict[c] = char_dict.setdefault(c, 0) + 1
     
    return char_dict

def strip_non_alpha_from_dict(dictionary):
    alpha_dict = {key: value for key, value in dictionary.items() if key.isalpha()}
    return alpha_dict

def sort_dict(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[-1], reverse=True))
    return sorted_dict
    
