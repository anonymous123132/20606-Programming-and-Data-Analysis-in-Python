def decoding(s):
    s = s.lstrip().rstrip()
    s = s.replace("***", " ")
    s = s.replace("^", "\n")
    s = s.capitalize()
    return s