'''
Day 11: Enunciado
El grinch quiere robar los regalos de Navidad del almacén. Para ello
necesita saber qué regalos no tienen vigilancia.

El almacén se representa como un array de strings (string[]), donde
cada regalo (*) está protegido si su posición está junto a una cámara
(#). Cada espacio vacío se representa con un punto (.).

Tu tarea es contar cuántos regalos están sin vigilancia, es decir, que
no tienen ninguna cámara adyacente (arriba, abajo, izquierda o derecha).

Ten en cuenta: solo se considera como "adyacente" las 4 direcciones
cardinales, no en diagonal.

Los regalos en las esquinas o bordes pueden estar sin vigilancia, siempre
que no tengan cámaras directamente al lado.

findUnsafeGifts([
  '.*.',
  '*#*',
  '.*.'
]) // ➞ 0

// Todos los regalos están junto a una cámara

findUnsafeGifts([
  '...',
  '.*.',
  '...'
]) // ➞ 1

// Este regalo no tiene cámaras alrededor

findUnsafeGifts([
  '*.*',
  '...',
  '*#*'
]) // ➞ 2
// Los regalos en las esquinas superiores no tienen cámaras alrededor

findUnsafeGifts([
  '.....',
  '.*.*.',
  '..#..',
  '.*.*.',
  '.....'
]) // ➞ 4

// Los cuatro regalos no tienen cámaras, porque están en diagonal a la cámara
'''

#Versión de 4 estrellas
def find_unsafe_gifts(warehouse: list[str]) -> int:

  unsafe_gifts = 0

  for posY, line in enumerate(warehouse):
    for posX, char in enumerate(line):
      safe_gift = False

      if char == '*':
        # UP
        if (posY - 1) >= 0:
          if warehouse[posY - 1][posX] == '#':
            safe_gift = True
        # DOWN
        if (posY + 1) < len(warehouse):
          if warehouse[posY + 1][posX] == '#':
            safe_gift = True
        # LEFT
        if (posX - 1) >= 0:
          if warehouse[posY][posX - 1] == '#':
            safe_gift = True
        # RIGHT
        if (posX + 1) < len(line):
          if warehouse[posY][posX + 1] == '#':
            safe_gift = True

        # UNSAVED
        if safe_gift == False:
          unsafe_gifts += 1


  return unsafe_gifts

'''
unsafe_gifts = find_unsafe_gifts([
  '...#....',
  '..*#*..',
  '...#....'
])
# ➞ 0
# Todos los regalos están junto a una cámara
print(unsafe_gifts)'''


unsafe_gifts = find_unsafe_gifts([
  '.*.',
  '*#*',
  '.*.'
])
# ➞ 0
# Todos los regalos están junto a una cámara
print(unsafe_gifts)

unsafe_gifts2 = find_unsafe_gifts([
  '...',
  '.*.',
  '...'
]) 
# ➞ 1
# Este regalo no tiene cámaras alrededor
print(unsafe_gifts2)

unsafe_gifts3 = find_unsafe_gifts([
  '*.*',
  '...',
  '*#*'
]) 
# ➞ 2
# Los regalos en las esquinas superiores no tienen cámaras alrededor
print(unsafe_gifts3)

unsafe_gifts4 = find_unsafe_gifts([
  '.....',
  '.*.*.',
  '..#..',
  '.*.*.',
  '.....'
]) 
# ➞ 4
# Los cuatro regalos no tienen cámaras, porque están en diagonal a la cámara
print(unsafe_gifts4)