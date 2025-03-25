def get_num_words(book_content):
    num_words = book_content.split()
    return len(num_words)

def get_character_counts(book_content):
    char_dict = {}
    for char in book_content:
        char = char.lower()
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def get_sorted_counts(dictionary):

    sorted_dict = {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1], reverse=True)}
    return sorted_dict