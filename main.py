###solution to exercise 93 from ben stephenson's "the python workbook".

def is_prime(num):
  if num == 1:
    return True
  elif num == 2:
    return True   
  else:
    result = True
    for i in range(2, num // 2 + 1):
      if not (num % i):
        result = False
        break
    return result

num = int(input('Enter an integer: '))
next_num = num + 1
while not is_prime(next_num):
  next_num += 1
print(next_num)
