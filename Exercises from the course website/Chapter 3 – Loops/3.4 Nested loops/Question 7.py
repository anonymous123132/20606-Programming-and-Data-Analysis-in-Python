s = input("Please enter string: ")
answer = ""
for i in range(len(s)):
      for j in range(i + 2, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                  answer += substring + " "
print(answer)