"""Given an integer, , print the following values for each integer  from  to :

Decimal
Octal
Hexadecimal (capitalized)
Binary
"""

def print_formatted(number):
  width = len(bin(number)) - 2
  for i in range(1 , number + 1):
    print(f"{i:>{width}d} {i:>{width}o} {i:>{width}X} {i:>{width}b}")

if __name__ == '__main__':