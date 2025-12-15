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

# Versión de 4 estrellas
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
    tree  = tree + f"{row.center(margin)}".rstrip() + '\n'

  return tree.rstrip()

'''
Puntos fuertes:
• La lógica para construir las filas del árbol es correcta y maneja la frecuencia de los
adornos adecuadamente.
• El centrado de las filas y la adición del tronco son implementados de forma correcta.
• El código es legible y utiliza nombres de variables descriptivos.
Puntos a mejorar:
• La variable `freq_count` se reinicia incorrectamente dentro del bucle interno, lo que
afecta la lógica de la frecuencia de los adornos. Debería ser un contador global para todo
el árbol.
Próximos pasos:
• Corregir la lógica de `freq_count` para que sea un contador acumulativo a lo largo de
todas las filas del árbol, no solo por fila. Esto asegurará que los adornos se coloquen en
las posiciones correctas según la frecuencia especificada.
'''
'''
Puntos fuertes:
• La lógica para construir el árbol y manejar la frecuencia de los adornos es correcta.
• El uso de `center()` para centrar las filas y `rstrip()` para eliminar espacios finales
es apropiado.
• La variable `freq_count` rastrea correctamente la posición global de los adornos.
Puntos a mejorar:
• La construcción de cadenas de texto (`symbol_row = symbol_row + '*'`) dentro de bucles puede
ser ineficiente en Python. Se recomienda usar `str.join()` para mejorar el rendimiento.
Próximos pasos:
• Reemplazar la concatenación de cadenas dentro de los bucles por `str.join()` para mejorar la
eficiencia.
'''
'''
Puntos fuertes:
• La lógica para generar los adornos y asteriscos es correcta y maneja la frecuencia adecuadamente.
• El centrado de las filas y la adición del tronco son implementados de forma correcta.
• El código es legible y utiliza nombres de variables descriptivos.
Puntos a mejorar:
• La construcción de la cadena `tree` mediante concatenación repetida (`tree = tree + ...`) dentro
de un bucle puede ser ineficiente para árboles muy grandes. Se recomienda usar `' '.join(rows)`
para una mejor performance.
Próximos pasos:
• Considerar reemplazar la concatenación de cadenas en el bucle final por `' '.join(rows)` para
mejorar la eficiencia.
'''
# Versión de 4 estrellas
def draw_tree2(height, ornament, frequency):

  row = 1
  freq_count = 1
  rows = []
  tree = []

  for i in range(height):
    symbols = []
    
    for j in range(row):
      if freq_count % frequency != 0:
        symbols.append('*')
      else:
        symbols.append(ornament)

      freq_count +=1

    symbol_row = ''.join(symbols)
    rows.append(symbol_row)
    row += 2

  margin = row - 2
  rows.append('#')

  for row in rows:
    tree.append(f"{row.center(margin)}".rstrip())

  return_tree = '\n'.join(tree)

  return return_tree.rstrip()

tree = draw_tree2(6, '@', 4)
print(tree)