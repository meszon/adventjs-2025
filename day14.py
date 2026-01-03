'''
Day 14: Enunciado
En el Polo Norte, los elfos han simplificado su sistema de almacenamiento
para evitar errores.
Ahora guardan los regalos en un objeto mágico con profundidad limitada,
donde cada valor aparece una sola vez.

Santa necesita una forma rápida de saber qué camino de claves debe seguir
para encontrar un regalo concreto.

Tu tarea es escribir una función que, dado un objeto y un valor, devuelva
el array de claves que hay que recorrer para llegar a ese valor.

Reglas:

El objeto tiene como máximo 3 niveles de profundidad.
El valor a buscar aparece como mucho una vez.
El objeto solo contiene otros objetos y valores primitivos (strings, numbers,
booleans).
Si el valor no existe, devuelve un array vacío.
Ejemplos:

const workshop = {
  storage: {
    shelf: {
      box1: 'train',
      box2: 'switch'
    },
    box: 'car'
  },
  gift: 'doll'
}

findGiftPath(workshop, 'train')
// ➜ ['storage', 'shelf', 'box1']

findGiftPath(workshop, 'switch')
// ➜ ['storage', 'shelf', 'box2']

findGiftPath(workshop, 'car')
// ➜ ['storage', 'box']

findGiftPath(workshop, 'doll')
// ➜ ['gift']

findGiftPath(workshop, 'plane')
// ➜ []
'''

#Versión de 4 estrellas
def find_gift_path(workshop: dict, gift: str | int | bool) -> list[str]:

    for key, value in workshop.items():
        if value == gift:
            return [key]
        
        if isinstance(value, dict):
            for key2, value2 in value.items():
                if value2 == gift:
                    return [key, key2]
                
                if isinstance(value2, dict):
                    for key3, value3 in value2.items():
                        if value3 == gift:
                            return [key, key2, key3]


    return []

workshop = {
    'storage': {
        'shelf': {
            'box1': 'train',
            'box2': 'switch'
        },
        'box': 'car'
    },
    'gift': 'doll'
}

path = find_gift_path(workshop, 'train')
# ➜ ['storage', 'shelf', 'box1']
print(path)

path2 = find_gift_path(workshop, 'switch')
# ➜ ['storage', 'shelf', 'box2']
print(path2)

path3 = find_gift_path(workshop, 'car')
# ➜ ['storage', 'box']
print(path3)

path4 = find_gift_path(workshop, 'doll')
# ➜ ['gift']
print(path4)

path5 =find_gift_path(workshop, 'plane')
# ➜ []
print(path5)