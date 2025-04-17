def rotate_string_right(s,r):
    num = len(s)//r
    return s[-num:] + s[:-num]

print(rotate_string_right('abcd',2))