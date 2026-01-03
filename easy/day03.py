'''
Day 3: Enunciado
En el taller de Santa hay un elfo becario que está aprendiendo a envolver regalos.

Le han pedido que envuelva cajas usando solo texto… y lo hace más o menos bien.

Le pasan dos parámetros:

size: el tamaño del regalo cuadrado
symbol: el carácter que el elfo usa para hacer el borde (cuando no se equivoca)
El regalo debe cumplir:

Debe ser un cuadrado de size x size.
El interior siempre está vacío (lleno de espacios), porque el elfo "aún no sabe 
dibujar el relleno".
Si size < 2, devuelve una cadena vacía: el elfo lo intentó, pero se le perdió el regalo.
El resultado final debe ser un string con saltos de línea \n.
Sí, es un reto fácil… pero no queremos que despidan al becario. ¿Verdad?

Ejemplos
const g1 = drawGift(4, '*')
console.log(g1)
/*
 ****
 *  *
 *  *
 ****
 */

const g2 = drawGift(3, '#')
console.log(g2)
/*
###
# #
###
*/

const g3 = drawGift(2, '-')
console.log(g3)
/*
--
--
*/

const g4 = drawGift(1, '+')
console.log(g4)
// ""  pobre becario…
'''
# Versión de 3 estrellas
def draw_gift(size, symbol):
    if size < 2:
        return ''
    else:
        draw = symbol * size
        draw_loop = ''

        for row in range(size - 2):
            i = 0
            while i < size:
                if i == 0 or i == (size - 1):
                    draw_loop = draw_loop + symbol
                else:
                    draw_loop = draw_loop + " "
                i = i + 1
            draw_loop = draw_loop + '\n'
        
        return draw  + '\n' + draw_loop + draw

# Versión de 5 estrellas
def draw_gift2(size, symbol):
    if size < 2:
        return ''
    else:
        draw = []
        draw_all = symbol * size
        draw.append(draw_all)
        draw_empty = symbol + (' ') * (size - 2) + symbol
        
        for i in range(size - 2):
            draw.append(draw_empty)
        
        draw.append(draw_all)
        return '\n'.join(draw)        


print(draw_gift2(3, '#'))
