def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()
        number_words = count_words(text)
        print(f"The book contains {number_words} words.")
        number_chars = count_chars(text)
        print(f"The book contains the following letters (alphabetically):")
        print_chars(number_chars)
        number_chars = sort_by_appearance(number_chars)
        print(f"The book contains the following letters (falling order):")
        print_chars(number_chars)


def count_words(text: str) -> int:
    """Takes a string as input and returns the number of words of that given string as an integer"""
    return len(text.split())

def count_chars(text: str) -> dict:
    """Takes a string as input and returns a dictionary of how often each letter appears
    within the given string (alphabetical order)"""
    list_of_chars = {}
    text = text.lower()
    for char in text:
        if char.isalpha():
            if char in list_of_chars:
                list_of_chars[char] += 1
            else:
                list_of_chars[char] = 1
    lsit_of_chars_ordered = dict(sorted(list_of_chars.items()))
    return lsit_of_chars_ordered

def sort_by_appearance(chars: dict) -> dict:
    """Takes a dict as input and returns it sorted by the key-value"""
    return dict(sorted(chars.items(), key=lambda item: item[1], reverse=True))

def print_chars(list_of_chars: dict) -> None:
    for key,value in list_of_chars.items():
            print(f"{key} -> {value}")
main()