def get_number_of_words(text):
    words = text.split()
    return len(words)

def get_number_of_characters(text):
    text_lower = text.lower()
    characters = {}
    for char in text_lower:
        if char.isalpha():
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    return characters

def sort_characters_by_frequency(char_dict):
    return dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))
