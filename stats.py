def num_words(full_text):
    words = full_text.split()
    wordcount = len(words)
    return wordcount

def char_count(full_text):
    characters = {}
    lower_case = full_text.lower()
    for char in set(lower_case):
        characters[char] = lower_case.count(char)
    return characters   
   
def sort_chars(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "count": count})

    def sort_on(dict):
        return dict["count"]
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list

