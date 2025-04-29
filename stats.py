def get_book_word_count(book_string):
    return len(book_string.split())


def get_character_count(book_string):
    character_dict = {}
    lower_book_string = book_string.lower()

    for letter in lower_book_string:
        if letter in character_dict:
            character_dict[letter] += 1
        else:
            character_dict[letter] = 1
    
    return character_dict


def sort_on(dict):
    return dict["num"]


def get_sorted_dicts(character_dict):
    character_list = []

    for key, value in character_dict.items():
        character_list.append({"char": key, "num": value})
    
    character_list.sort(reverse=True, key=sort_on)

    return character_list
