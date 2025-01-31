def main():
    file_contents = ""
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    def get_word_count(book):
        word_list = book.split()
        word_count = 0
        for word in word_list:
            word_count += 1
        return word_count
    
    def get_character_count(book):
        character_count = {}
        full_lower_case = book.lower()
        for character in full_lower_case:
            if character in character_count:
                character_count[character] += 1
            else:
                character_count[character] = 1
        return character_count


    word_count = (get_word_count(file_contents))
    character_count = get_character_count(file_contents)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
   
    print("---- Begin Report of Document ----")
    print(f"{word_count} words found in document")
    for character in character_count:
        if character in alphabet:
            print(f"The '{character}' was found {character_count[character]} times")
    print("---- End Report ----")




main()