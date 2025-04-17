def word(s):
  chars = 0
  words = 1
  sentences = 0
  for ch in s:
      if ch.islower() or ch.isupper():
          chars += 1
      elif ch.isspace():
          words += 1
      elif ch == '.':
          sentences += 1
  return str(chars) +", " + str(words) + ", " + str(sentences)