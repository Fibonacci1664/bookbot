from stats import get_book_word_count, get_book_character_count,sort_dict

def get_book_text(file_path) -> str:

    book_text = ""

    with open(file_path) as f:
        book_text = f.read()
    
    return book_text

def print_report(path, word_count, sorted_list) -> str:

    print(f"============ BOOKBOT ===========\n" \
          f"Analysing book found at {path}...\n" \
          f"----------- Word Count -----------\n" \
          f"Found {word_count} total words\n" \
          f"--------- Character Count ---------")
    
    for item in sorted_list:
        print(f"{item["char"]}: {item["num"]}")

    print("============ END ===========")

def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)  
    char_count = get_book_character_count(text)
    word_count = get_book_word_count(text)

    sorted_list = sort_dict(char_count)
    print_report(file_path, word_count, sorted_list)

if __name__ == "__main__":
    main()