from itertools import permutations  
  
def p24(n):
  return "".join(list(map(str, list(permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))[n])))

print(p24((10 ** 6) - 1))

