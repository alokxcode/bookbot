from stats import count_words, count_characters, sort_dict

def get_book_text(file_path):
    with open(file_path) as f:
        book_contents = f.read()
    return book_contents


def main(file_path):
    book_contents = get_book_text(file_path)
    msg = count_words(book_contents)
    counting_characters = count_characters(book_contents)
    sorted_characters_num = sort_dict(counting_characters)

    print('==============================  BookBot  ==============================')
    print(f'Analyzing Book found at {file_path}')
    print('     ------------------------  Word Count  -----------------------     ')
    print(msg)
    print('     ---------------------  Characters Count  --------------------     ')
    for characters in sorted_characters_num:
        print(f'{characters['char']} : {characters['num']}')
    print('================================  End  ================================')

def run():
    import sys
    if len(sys.argv) <= 1 or len(sys.argv) > 2:
        print(f'Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    else:
        main(sys.argv[1])
    
run()