def is_perfect(n):
  if n < 2:
    return False
  divisors_sum = 1
  for item in range(2, n):
      if n % item == 0:
          divisors_sum += item
  return divisors_sum == n

def find_perfects_in_range(start, end):
  answer = ""
  for item in range(start, end + 1):
      if is_perfect(item):
          answer += str(item) + " "
  return answer