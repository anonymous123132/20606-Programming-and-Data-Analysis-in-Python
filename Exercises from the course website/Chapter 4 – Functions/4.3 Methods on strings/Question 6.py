def encoding(s, n):
    answer = ""
    for ch in s:
        answer += chr(ord(ch) + n)
    return answer