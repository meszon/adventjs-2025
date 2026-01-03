'''
Day 6: Enunciado
En el taller de Santa, los elfos han encontrado una montaña de guantes mágicos
totalmente desordenados. Cada guante viene descrito por dos valores:

hand: indica si es un guante izquierdo (L) o derecho (R)
color: el color del guante (string)
Tu tarea es ayudarles a emparejar guantes: Un par válido es un guante izquierdo
y uno derecho del mismo color.

Debes devolver una lista con los colores de todos los pares encontrados. Ten en
cuenta que puede haber varios pares del mismo color. El orden se determina por
el que se pueda hacer primero el par.

Ejemplos
const gloves = [
  { hand: 'L', color: 'red' },
  { hand: 'R', color: 'red' },
  { hand: 'R', color: 'green' },
  { hand: 'L', color: 'blue' },
  { hand: 'L', color: 'green' }
]

matchGloves(gloves)
// ["red", "green"]

const gloves2 = [
  { hand: 'L', color: 'gold' },
  { hand: 'R', color: 'gold' },
  { hand: 'L', color: 'gold' },
  { hand: 'L', color: 'gold' },
  { hand: 'R', color: 'gold' }
]

matchGloves(gloves2)
// ["gold", "gold"]

const gloves3 = [
  { hand: 'L', color: 'red' },
  { hand: 'R', color: 'green' },
  { hand: 'L', color: 'blue' }
]

matchGloves(gloves3)
// []

const gloves4 = [
  { hand: 'L', color: 'green' },
  { hand: 'L', color: 'red' },
  { hand: 'R', color: 'red' },
  { hand: 'R', color: 'green' }
]

matchGloves(gloves4)
// ['red', 'green']
'''
from typing import List, Dict

#Versión de 3 estrellas
def match_gloves(gloves: List[Dict[str, str]]) -> List[str]:

    for index, glove in enumerate(gloves):
        glove['index'] = index

    left_gloves = [glove for glove in gloves if glove['hand'] == 'L']
    right_gloves = [glove for glove in gloves if glove['hand'] == 'R']

    color_match = []
    pair = False
    loop2_counter = 0

    for glove in left_gloves:
        color = glove['color']
        index = glove['index']

        for loop2, glove2 in enumerate(right_gloves):
            color2 = glove2['color']
            index2 = glove2['index']

            if color == color2:
                priority = abs(index2 - index)
                color_match.append((color, priority))
                loop2_counter = loop2
                pair = True
                break
        
        if pair:
            pair = False
            right_gloves.remove(right_gloves[loop2_counter])
    
    colors = sorted(color_match, key=lambda tup:tup[1])
    colors = [color[0] for color in colors]

    return colors

'''
Puntos fuertes:
• El código intenta resolver el problema de emparejar guantes.
• Se utilizan comprensiones de lista para separar guantes izquierdos y derechos, lo cual es conciso.
Puntos a mejorar:
• La lógica para emparejar guantes es ineficiente y propensa a errores. Modificar `right_gloves` mientras
se itera sobre él puede llevar a resultados inesperados.
• La adición de una clave 'index' a los diccionarios de entrada modifica la estructura de datos original,
lo cual es un efecto secundario no deseado.
• El uso de `loop2_counter` y `pair` para controlar el flujo del bucle es confuso y poco idiomático en Python.
• La forma en que se calcula la 'prioridad' y se ordena `color_match` no garantiza el orden de emparejamiento
correcto según la descripción del problema (el orden se determina por el que se puede hacer primero el par).
• La complejidad temporal es alta debido a la anidación de bucles y la operación `remove` en una lista.
Próximos pasos:
• Reimplementar la lógica de emparejamiento para ser más eficiente y clara. Considerar el uso de diccionarios
para contar guantes por color y mano.
• Evitar modificar la lista de entrada o las sublistas de forma inesperada. Crear nuevas estructuras de datos
si es necesario.
• Simplificar el control de flujo del bucle. Eliminar variables auxiliares como `pair` y `loop2_counter` si es
posible.
• Asegurarse de que el orden de los pares devueltos coincida con el orden en que se forman los pares en la lista
de entrada.
• Mejorar la eficiencia algorítmica. Una solución con complejidad O(N) o O(N log N) sería preferible a la actual
O(N^2).
'''
def match_gloves2(gloves: List[Dict[str, str]]) -> List[str]:
    return []

gloves = [
    { 'hand': 'L', 'color': 'red' },
    { 'hand': 'R', 'color': 'red' },
    { 'hand': 'R', 'color': 'green' },
    { 'hand': 'L', 'color': 'blue' },
    { 'hand': 'L', 'color': 'green' }
]
colors = match_gloves(gloves)
# ["red", "green"]
print(colors)

gloves2 = [
    { 'hand': 'L', 'color': 'gold' },
    { 'hand': 'R', 'color': 'gold' },
    { 'hand': 'L', 'color': 'gold' },
    { 'hand': 'L', 'color': 'gold' },
    { 'hand': 'R', 'color': 'gold' }
]
colors2 = match_gloves(gloves2)
# ["gold", "gold"]
print(colors2)

gloves3 = [
    { 'hand': 'L', 'color': 'red' },
    { 'hand': 'R', 'color': 'green' },
    { 'hand': 'L', 'color': 'blue' }
]
colors3 = match_gloves(gloves3)
# []
print(colors3)

gloves4 = [
    { 'hand': 'L', 'color': 'green' },
    { 'hand': 'L', 'color': 'red' },
    { 'hand': 'R', 'color': 'red' },
    { 'hand': 'R', 'color': 'green' }
]
colors4 = match_gloves(gloves4)
# ['red', 'green']
print(colors4)