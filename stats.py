def get_word_count(text):
    words = text.split()
    total_words = len(words)
    return total_words

def get_char_count(characters):
    lower_chars = characters.lower()

    count = {}
    for c in lower_chars:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    return count

def sort_on(dict):
    return dict["num"]

def get_char_list_from_dict(dict):
    empty_list = []
    for i in dict:
        if i.isalpha():
            num = dict[i]
            new_dict = {"char": i, "num": num}
            empty_list.append(new_dict)
    empty_list.sort(reverse=True, key=sort_on)
    return empty_list
