'''
Day 15: Enunciado
Al Polo Norte ha llegado ChatGPT y el elfo Sam Elfman está trabajando en una aplicación
de administración de regalos y niños.

Para mejorar la presentación, quiere crear una función drawTable que reciba un array de
objetos y lo convierta en una tabla de texto.

La tabla dibujada debe tener:

Cabecera con letras de columna (A, B, C…).
El contenido de la tabla son los valores de los objetos.
Los valores deben estar alineados a la izquierda.
Los campos dejan siempre un espacio a la izquierda.
Los campos dejan a la derecha el espacio necesario para alinear la caja.
La función recibe un segundo parámetro sortBy que indica el nombre del campo por el que
se deben ordenar las filas. El orden será alfabético ascendente si los valores son
strings y numérico ascendente si son números.

Mira el ejemplo para ver cómo debes dibujar la tabla:

drawTable(
  [
    { name: 'Charlie', city: 'New York' },
    { name: 'Alice', city: 'London' },
    { name: 'Bob', city: 'Paris' }
  ],
  'name'
)
// +---------+----------+
// | A       | B        |
// +---------+----------+
// | Alice   | London   |
// | Bob     | Paris    |
// | Charlie | New York |
// +---------+----------+

drawTable(
  [
    { gift: 'Book', quantity: 5 },
    { gift: 'Music CD', quantity: 1 },
    { gift: 'Doll', quantity: 10 }
  ],
  'quantity'
)
// +----------+----+
// | A        | B  |
// +----------+----+
// | Music CD | 1  |
// | Book     | 5  |
// | Doll     | 10 |
// +----------+----+
'''

#Versión de 4 estrellas
def draw_table(data: list[dict[str, str | int]], sortBy: str) -> str:

    if not data:
        return ''
    
    table = sorted(data, key=lambda item:item[sortBy])
    max_char = [0] * len(table[0])
    table_items = []

    for row in table:
        items = [item for item in row.values()]
        for count, item in enumerate(items):
            if isinstance(item, int) or isinstance(item, bool):
                item = str(item)
            if len(item) > max_char[count]:
                max_char[count] = len(item)
        table_items.append(items)

    head = ''
    line = ''
    for number in range(len(table[0])):
        spacing = max_char[number] - len(chr(65 + number))
        head += '| ' + chr(65 + number) +  ' ' * (spacing + 1)
        line += '+' + '-' * (max_char[number] + 2)
    head += '|\n'
    line += '+'

    rows = ''
    for items in table_items:
        for count, item in enumerate(items):
            if isinstance(item, int) or isinstance(item, bool):
                item = str(item)
            spacing = max_char[count] - len(item)
            rows += '| ' + item + ' ' * (spacing + 1)
        rows += '|\n'
    
    return str(line + '\n' + head + line + '\n' + rows + line)

table = draw_table(
  [
    { 'name': 'Charlie', 'city': 'New York' },
    { 'name': 'Alice', 'city': 'London' },
    { 'name': 'Bob', 'city': 'Paris' }
  ],
  'name'
)
print(table)

table2 = draw_table(
  [
    { 'gift': 'Book', 'quantity': 5 },
    { 'gift': 'Music CD', 'quantity': 1 },
    { 'gift': 'Doll', 'quantity': 10 }
  ],
  'quantity'
)
print(table2)

table3 = draw_table(
[
    { 'a': 2, 'b': 'Y', 'c': 'X' },
    { 'a': 1, 'b': 'Z', 'c': 'W' },
    { 'a': 3, 'b': 'A', 'c': 'B' }
    ], 
    'a'
)
print(table3)

table4 = draw_table(
[
    { 'id': 'zebra', 'active': True },
    { 'id': 'alpha', 'active': False }
    ],
    'id'
)
print(table4)