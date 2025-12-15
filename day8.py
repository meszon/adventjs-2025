'''
Day 8: Enunciado
Santa quiere saber cuál es la primera letra no repetida en el nombre de un juguete.

Escribe una función que reciba un string y devuelva la primera letra que no se repite,
ignorando mayúsculas y minúsculas al contar, pero devolviendo la letra tal como aparece
en el string.

Si no hay ninguna, devuelve una cadena vacía ("").

Ejemplos:

findUniqueToy('Gift') // 'G'
// La G es la primera letra que no se repite
// y la devolvemos tal y como aparece

findUniqueToy('sS') // ''
// Las letras se repiten, ya que no diferencia mayúsculas

findUniqueToy('reindeeR') // 'i'
// La r se repite (aunque sea en mayúscula)
// y la e también, así que la primera es la 'i'

// Más casos:
findUniqueToy('AaBbCc') // ''
findUniqueToy('abcDEF') // 'a'
findUniqueToy('aAaAaAF') // 'F'
findUniqueToy('sTreSS') // 'T'
findUniqueToy('z') // 'z'
'''

#Versión de 5 estrellas
def find_unique_toy(toy: str) -> str:
  
  for letter in toy:
    if toy.lower().count(letter.lower()) == 1:
      return letter
  
  return ''

letter = find_unique_toy('AaBbCc')
# ''
print(letter)

letter2 = find_unique_toy('abcDEF')
# 'a'
print(letter2)

letter3 = find_unique_toy('aAaAaAF')
# 'F'
print(letter3)

letter4 = find_unique_toy('sTreSS')
# 'T'
print(letter4)

letter5 = find_unique_toy('z')
# 'z'
print(letter5)
