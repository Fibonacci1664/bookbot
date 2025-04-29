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

def sort_dict(dictionary) ->list[dict[str:int]]:
    dict_list = []
    
    #sort by value, use a lamda to get the second value i.e. [1] from a tuple

    # List of tuples
    dict_view = dictionary.items()

    sorted_list = sorted(dict_view, key=lambda tup: tup[1], reverse=True)

    for tup in sorted_list:
        if tup[0].isalpha():
            temp_dict = {"char": tup[0], "num": tup[1]}
            dict_list.append(temp_dict)

    return dict_list