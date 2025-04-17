def capitalize_words(string):
    string = string.split()
    for i in range(len(string)):
        string[i] = string[i].capitalize()
    return ' '.join(string)
