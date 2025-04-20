from stats import get_book_word_count, get_book_character_count

def get_book_text(file_path) -> str:

    book_text = ""

    with open(file_path) as f:
        book_text = f.read()
    
    return book_text

def main():
    text = get_book_text("books/frankenstein.txt")  
    char_count = get_book_character_count(text)
    word_count = get_book_word_count(text)

    print(f"{word_count} words found in the document")
    print(char_count)

if __name__ == "__main__":
    main()