

# 1. Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

def sum_to(n):
  print(sum(range(1, n+1)))

sum_to(6)
sum_to(2)


# 2. Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

def largest(list):
  return max(list)

print(largest([9999, 12, 2, 7, 4, 64, 73, 99, 200, 1000000]))
print(largest([9999, 12, 201]))

# 3. Write a function named `occurances` that takes two string arguments as input and counts the number of occurances of the second string inside the first string.

def occurances(str1, str2):
  return str1.count(str2)

print(occurances('beep bep', 'e'))
print(occurances('bazooka joe is cool', 'o'))


# 4. Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product. HINT: Review your notes on args.

def product(*args):
    numero = 1
    for n in args:
      numero *= n
    return numero

print(product(1, 2, 0))
print(product(1, 2, 10, 999, 20, 345, 666, 999, 66))
print(product(1, 2, 10, 999, 20, 345, 666, 999, 66, 0))
