def count_words(book_contents):
    total_words = book_contents.split()
    count = 0
    for i in total_words:
        count = count + 1
    return f'Found {count} Total words'

def count_characters(book_contents):
    book_contents = book_contents.lower()
    characters_array = ['.', '!', '?', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    characters_dict = {}
    for i in book_contents:
        for j in characters_array:
            if i == j:
                if j in characters_dict:
                    characters_dict[j] = characters_dict[j] + 1
                else:
                    characters_dict[j] = 1

    return characters_dict

def sort_on(items):
    return items['num']

def sort_dict(characters_dict):
    characters_num_array = []
    for key in characters_dict:
        characters_num_array.append({'char': key, 'num': characters_dict[key]})
        
    characters_num_array.sort(reverse=True, key=sort_on)

    return characters_num_array
