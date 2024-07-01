def main():
    characters = {}
    path = "books/frankenstein.txt"
    
    with open(path) as f:
        content = f.read()
    
    words_counted = count_words(content)
    character_counted = character_count(content)
    
    lista = [{"char": char, "qty":val} for char, val in character_counted.items() if char.isalpha()]
    
    lista.sort(reverse=True, key=sort_on)
    
    print(f"--- Begin report of {path} ---")
    print(f"{words_counted} words found in the document \n")
    
    for val in lista:
        print(f"The '{val['char']}' character was found {val['qty']} times")

    print(f"--- End report ---")

def count_words(content):
    words = content.split()
    return len(words)

def character_count(content):
    content_lower = content.lower()
    counted_chars_dict = {}
    
    for char in content_lower:
        if char in counted_chars_dict:
            counted_chars_dict[char] += 1
        else:
            counted_chars_dict[char] = 1
    
    return counted_chars_dict

def sort_on(dict):
    return dict["qty"]

main()