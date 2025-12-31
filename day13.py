'''
Day 13: Enunciado
Simula el recorrido de un regalo dentro de una fábrica y devuelve cómo termina.
Para ello debes crear una función runFactory(factory).

factory es un string[] donde cada celda puede ser:

> < ^ v movimientos
. salida correcta
Ten en cuenta que todas las filas tienen la misma longitud y que no habrá otros
símbolos.

El regalo siempre empieza en la posición (0,0) (arriba a la izquierda). En cada
paso lee la celda actual y se mueve según la dirección. Si llega a una celda con
un punto (.) significa que ha salido correctamente de la fábrica.

Resultado

Devuelve uno de estos valores:

'completed' si llega a un .
'loop' si visita una posición dos veces
'broken' si sale fuera del tablero

Ejemplos

runFactory([
  '>>.'
]) // 'completed'

runFactory([
  '>>>'
]) // 'broken'

runFactory([
  '>><'
]) // 'loop'

runFactory([
  '>>v',
  '..<'
]) // 'completed'

runFactory([
  '>>v',
  '<<<'
]) // 'broken'

runFactory([
  '>v.',
  '^..'
]) // 'completed'

runFactory([
  'v.',
  '^.'
]) // 'loop'
'''

#Versión de 3 estrellas
def run_factory(factory: list[str]) -> str:

    visited = []
    posY = 0
    posX = 0

    while (posY < len(factory)):
        line = factory[posY]
        while (posX < len(line)):
            char = line[posX]
            if (posY, posX) in visited:
                return 'loop'
            else:
                visited.append((posY, posX))
                match(char):
                    case '.':
                        return 'completed'
                    case '>':
                        posX += 1
                        if posX == len(line):
                            return 'broken'
                    case '<':
                        posX -= 1
                        if posX < 0:
                            return 'broken'
                    case 'v':
                        posY += 1
                        if posY == len(factory):
                            return 'broken'
                        break
                    case '^':
                        posY -= 1
                        if posY < 0:
                            return 'broken'
                        break

result = run_factory([
  '>>.'
])
# 'completed'
print(result)

result2 = run_factory([
  '>>>'
])
# 'broken'
print(result2)

result3 = run_factory([
  '>><'
])
# 'loop'
print(result3)

result4 = run_factory([
  '>>v',
  '..<'
])
# 'completed'
print(result4)

result5 = run_factory([
  '>>v',
  '<<<'
])
# 'broken'
print(result5)

result6 = run_factory([
  '>v.',
  '^..'
])
# 'completed'
print(result6)

result7 = run_factory([
  'v.',
  '^.'
])
# 'loop'
print(result7)