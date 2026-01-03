'''
Day 9: Enunciado
Los elfos han construido un reno robot aspirador (@) para limpiar un poco
el taller de cara a las navidades.

El reno se mueve sobre un tablero para recoger cosas del suelo (*) y debe evitar
obstáculos (#).

Recibirás dos parámetros:

board: un string que representa el tablero.
moves: un string con los movimientos: 'L' (izquierda), 'R' (derecha), 'U' (arriba),
'D' (abajo).
Reglas del movimiento:

Si el reno recoge algo del suelo (*) durante los movimientos → devuelve 'success'.
Si el reno se sale del tablero o choca contra un obstáculo (#) → devuelve 'crash'.
Si el reno no recoge nada ni se estrella → devuelve 'fail'.
Ten en cuenta que si el reno recoge algo del suelo, ya es 'success', indepentientemente
de si en movimientos posteriores se chocase con un obstáculo o saliese del tabler.

Importante: Ten en cuenta que en el board la primera y última línea están en blanco y
deben descartarse.

Ejemplo:

const board = `
.....
.*#.*
.@...
.....
`

moveReno(board, 'D')
// ➞ 'fail' -> se mueve pero no recoge nada

moveReno(board, 'U')
// ➞ 'success' -> recoge algo (*) justo encima

moveReno(board, 'RU')
// ➞ 'crash' -> choca contra un obstáculo (#)

moveReno(board, 'RRRUU')
// ➞ 'success' -> recoge algo (*)

moveReno(board, 'DD')
// ➞ 'crash' -> se choca con la parte de abajo del tablero

moveReno(board, 'UUU')
// ➞ 'success' -> recoge algo del suelo (*) y luego se choca por arriba

moveReno(board, 'RR')
// ➞ 'fail' -> se mueve pero no recoge nada
'''
from typing import List, Literal

#Versión de 4 estrellas
def move_reno(board: str, moves: str) -> Literal['fail', 'crash', 'success']:

  line_board = [line for line in board.split('\n') if line != '']
  char_board = [list(line) for line in line_board]

  robot_posX = -1
  robot_posY = -1

  for posY, line in enumerate(char_board):
    for posX, char in enumerate(line):
      if char == '@':
        robot_posX = posX
        robot_posY = posY
        break
    if robot_posX != -1 and robot_posY != -1:
      break

  for movement in moves:
    match(movement):
      case 'R':
        robot_posX += 1
      case 'L':
        robot_posX -= 1
      case 'U':
        robot_posY -= 1
      case 'D':
        robot_posY += 1

    if robot_posX < 0 or robot_posY < 0 or robot_posX >= len(char_board[0]) or robot_posY >= len(char_board):
      return 'crash'
    
    match(char_board[robot_posY][robot_posX]):
      case '*':
        return 'success'

      case '#':
        return 'crash'

  return 'fail'

board = """
.....
.*#.*
.@...
.....
"""

'''
Puntos fuertes:
• La lógica para encontrar la posición inicial del robot es correcta.
• El manejo de los movimientos y la detección de colisiones/recogida son eficientes.
• El código es limpio y fácil de seguir para la mayoría de las operaciones.
Puntos a mejorar:
• La complejidad ciclomática es alta (18), lo que indica un flujo de control potencialmente
complejo. Se podría simplificar el uso de `match` anidado o condicionales.
Próximos pasos:
• Considerar refactorizar el bloque de `match` para los movimientos y la comprobación del
tablero para reducir la complejidad ciclomática. Por ejemplo, se podría separar la lógica de
movimiento de la lógica de comprobación de colisión/recogida.
'''

#Versión de 4 estrellas
def move_reno2(board: str, moves: str) -> Literal['fail', 'crash', 'success']:

  line_board = [line for line in board.split('\n') if line != '']
  char_board = [list(line) for line in line_board]

  robot_posX = -1
  robot_posY = -1

  for posY, line in enumerate(char_board):
    for posX, char in enumerate(line):
      if char == '@':
        robot_posX = posX
        robot_posY = posY
        break
    if robot_posX != -1 and robot_posY != -1:
      break

  for movement in moves:
    if movement == 'R':
      robot_posX += 1
    elif movement == 'L':
      robot_posX -= 1
    elif movement == 'U':
      robot_posY -= 1
    elif movement == 'D':
      robot_posY += 1

    if robot_posX < 0 or robot_posY < 0 or robot_posX >= len(char_board[0]) or robot_posY >= len(char_board):
      return 'crash'
    
    if char_board[robot_posY][robot_posX] == '*':
      return 'success'
    elif char_board[robot_posY][robot_posX] == '#':
      return 'crash'

  return 'fail'

info = move_reno(board, 'D')
# ➞ 'fail' -> se mueve pero no recoge nada
print(info)

info2 = move_reno(board, 'U')
# ➞ 'success' -> recoge algo (*) justo encima
print(info2)

info3 = move_reno(board, 'RU')
# ➞ 'crash' -> choca contra un obstáculo (#)
print(info3)

info4 = move_reno(board, 'RRRUU')
# ➞ 'success' -> recoge algo (*)
print(info4)

info5 = move_reno(board, 'DD')
# ➞ 'crash' -> se choca con la parte de abajo del tablero
print(info5)

info6 = move_reno(board, 'UUU')
# ➞ 'success' -> recoge algo del suelo (*) y luego se choca por arriba
print(info6)

info7 = move_reno(board, 'RR')
# ➞ 'fail' -> se mueve pero no recoge nada
print(info7)