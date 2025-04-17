def reverse_sentence(sentence):
    words = sentence.split(" ")
    words.reverse()
    words = " ".join(words)
    return words



print(reverse_sentence("Everything will be fine",))