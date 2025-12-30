'''
Day 10: Enunciado
Profundidad de Magia Navideña
En el Polo Norte, Santa Claus está revisando las cartas mágicas que recibe de
los niños de todo el mundo. Estas cartas usan un antiguo lenguaje navideño en
el que los corchetes [ y ] representan la intensidad del deseo.

Cuanto más profunda sea la anidación de los corchetes, más fuerte es el deseo.
Tu misión es averiguar la máxima profundidad en la que se anidan los [].

Pero ¡cuidado! Algunas cartas pueden estar mal escritas. Si los corchetes no
están correctamente balanceados (si se cierra antes de abrir, sobran cierres o
faltan cierres), la carta es inválida y debes devolver -1.

maxDepth('[]') // -> 1
maxDepth('[[]]') // -> 2
maxDepth('[][]') // -> 1
maxDepth('[[][]]') // -> 2
maxDepth('[[[]]]') // -> 3
maxDepth('[][[]][]') // -> 2

maxDepth('][') // -> -1 (cierra antes de abrir)
maxDepth('[[[') // -> -1 (faltan cierres)
maxDepth('[]]]') // -> -1 (sobran cierres)
maxDepth('[][][') // -> -1 (queda uno sin cerrar)
'''

#Versión de 3 estrellas
def max_depth(s: str) -> int:
    # Code here
    intensity = 0
    final_intensity = 0

    if s[0] == ']' or s == '':
        return - 1
    else:
        for char in s:
            if char == '[':
                intensity += 1
            if char == ']':
                if intensity > final_intensity:
                    final_intensity = intensity
                intensity -= 1

        if intensity != 0:
            return -1
        else:
            return final_intensity

intensity = max_depth('[]')
# -> 1
print(intensity)

intensity2 = max_depth('[[]]')
# -> 2
print(intensity2)

intensity3 = max_depth('[][]')
# -> 1
print(intensity3)

intensity4 = max_depth('[[][]]')
# -> 2
print(intensity4)

intensity5 = max_depth('[[[]]]')
# -> 3
print(intensity5)

intensity6 = max_depth('[][[]][]')
# -> 2
print(intensity6)

intensity7 = max_depth('][')
# -> -1 (cierra antes de abrir)
print(intensity7)

intensity8 = max_depth('[[[')
# -> -1 (faltan cierres)
print(intensity8)

intensity9 = max_depth('[]]]')
# -> -1 (sobran cierres)
print(intensity9)

intensity10 = max_depth('[][][')
# -> -1 (queda uno sin cerrar)
print(intensity10)