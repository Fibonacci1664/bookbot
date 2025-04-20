def get_book_word_count(text) -> int:

    num_of_words = 0
    word_list = text.split()
    num_of_words = len(word_list)

    return num_of_words

def get_book_character_count(text) -> dict[str, int]:
    char_count = {}
    low_text = text.lower()

    for char in low_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1 

    return char_count