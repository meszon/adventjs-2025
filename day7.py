'''
Day 7: Enunciado
¡Es hora de decorar el árbol de Navidad! Escribe una función que reciba:

height → la altura del árbol (número de filas).
ornament → el carácter del adorno (por ejemplo, "o" o "@").
frequency → cada cuántas posiciones de asterisco aparece el adorno.
El árbol se dibuja con asteriscos *, pero cada frequency posiciones, el
asterisco se reemplaza por el adorno.

El conteo de posiciones empieza en 1, desde la copa hasta la base, de
izquierda a derecha. Si frequency es 2, los adornos aparecen en las
posiciones 2, 4, 6, etc.

El árbol debe estar centrado y tener un tronco # de una línea al final.
Cuidado con los espacios en blanco, nunca hay al final de cada línea.

Ejemplos
drawTree(5, 'o', 2)
//     *
//    o*o
//   *o*o*
//  o*o*o*o
// *o*o*o*o*
//     #

drawTree(3, '@', 3)
//   *
//  *@*
// *@**@
//   #

drawTree(4, '+', 1)
//    +
//   +++
//  +++++
// +++++++
//    #
'''

# Versión de X estrellas
def draw_tree(height, ornament, frequency):

  row = 1
  freq_count = 1
  rows = []
  tree = ''

  for i in range(height):
    symbol_row = ''
    
    for j in range(row):
      if freq_count < frequency:
        symbol_row = symbol_row + '*'
      else:
        symbol_row = symbol_row + ornament
        freq_count = 0

      freq_count +=1

    rows.append(symbol_row)
    row += 2

  margin = row - 2
  rows.append('#')

  for row in rows:
    tree  = tree + f"{row.center(margin)}" + '\n'

  return tree.rstrip()

tree = draw_tree(6, '@', 4)
print(tree)