'''
Day 4: Enunciado
Los elfos han encontrado el código cifrado que protege la puerta del taller de Santa. 
El PIN tiene 4 dígitos, y está escondido dentro de bloques como estos:

[1++][2-][3+][<]
Escribe una función que descifre el PIN a partir del código.

El código está formado por bloques entre corchetes [...] y cada bloque genera un dígito del PIN.

Un bloque normal tiene la forma [nOP...], donde n es un número (0-9) y después puede haber una lista
de operaciones (opcionales).

Las operaciones se aplican en orden al número y son:

+ suma 1
- resta 1
El resultado siempre es un dígito (aritmética mod 10), por ejemplo 9 + 1 → 0 y 0 - 1 → 9.

También existe el bloque especial [<], que repite el dígito del bloque anterior.

Si al final hay menos de 4 dígitos, se debe devolver null.

Ejemplos
decodeSantaPin('[1++][2-][3+][<]')
// "3144"

decodeSantaPin('[9+][0-][4][<]')
// "0944"

decodeSantaPin('[1+][2-]')
// null (solo 2 dígitos)
'''
#Versión de 3 estrellas
def decode_santa_pin(code: str) -> str:
    code = code.replace(']', '').split('[')
    code = code [1:len(code)]
    results = []

    if code[0] == '<' or len(code) < 4:
        return None
    else: 
        char_counter = 0
        for chars in code:
            num = chars[0]
            if num == '<':
                results.append(str(results[char_counter - 1]))
            else:
                chars = chars[1:len(chars)]
                num = int(num)
                for char in chars:
                    if char == '+':
                        num = num + 1
                    if char == '-':
                        num = num - 1
                results.append(str(num % 10))
            char_counter = char_counter + 1
        return ''.join(results)

'''
Puntos fuertes:
• La lógica principal para procesar los bloques y aplicar las operaciones es correcta.
• Se maneja correctamente la aritmética modular para los dígitos.
• El código intenta manejar el caso especial del bloque '<'.
Puntos a mejorar:
• El código no maneja correctamente el caso en que el primer bloque sea '<'.
• El código no devuelve `null` si al final hay menos de 4 dígitos, solo si el primer bloque 
es '<' o la longitud total es menor a 4 (lo cual es incorrecto).
• La lógica para el bloque '<' no es robusta; asume que `char_counter - 1` siempre será un 
índice válido y no maneja el caso de un '<' al principio.
• Hay una asignación redundante `chars = chars[1:len(chars)]` después de haber extraído 
`num = chars[0]`.
Próximos pasos:
• Implementar la lógica para devolver `null` si el número total de dígitos generados es menor a 4.
• Corregir el manejo del bloque '<' para que funcione correctamente incluso si aparece después 
del primer dígito y para evitar errores de índice.
• Eliminar la asignación redundante `chars = chars[1:len(chars)]`.
'''
#Versión de 4 estrellas
def decode_santa_pin2(code: str) -> str:
    code = code.replace(']', '').split('[')
    code = code[1:len(code)]
    results = []
 
    for index, digit in enumerate(code):
        num = digit[0]
        match num:
            case '<':
                if index == 0:
                    return None
                else: 
                    results.append(results[-1])
            case _:
                num = int(digit[0])
                ops = digit[1:len(digit)]

                for op in ops:
                    match op:
                        case '+':
                            num += 1
                        case '-':
                            num -= 1

                results.append(str(num  % 10))
    if len(results) < 4:
        return None
    else:
        decrypted = ''.join(results)
        return decrypted
    
'''
Puntos fuertes:
• La lógica principal para decodificar el PIN es correcta y maneja las operaciones de suma y resta
de manera adecuada.
• El código maneja correctamente el bloque especial '<' para repetir el dígito anterior.
• Se verifica que el resultado final tenga al menos 4 dígitos, devolviendo `None` en caso contrario.
• El uso de `match` para las operaciones es moderno y legible.
Puntos a mejorar:
• La manipulación inicial de la cadena `code` (`code.replace(']', '').split('[')`) podría ser más
robusta y clara. Por ejemplo, un bloque vacío `[]` o un bloque mal formado `[abc]` podrían causar
errores inesperados.
• El manejo del caso `num == '<'` dentro del bucle `for` es un poco redundante. Podría simplificarse
la lógica de acceso al dígito anterior.
Próximos pasos:
• Considerar una forma más robusta de parsear los bloques, quizás usando expresiones regulares o iterando
sobre los caracteres para identificar los límites de los bloques de manera más explícita.
• Refactorizar la lógica del bloque '<' para evitar la comprobación `if index == 0` dentro del bucle,
haciendo que el acceso a `results[-1]` sea más directo cuando sea aplicable.
'''
import re

#Versión de 4 estrellas
def decode_santa_pin3(code: str) -> str:

    regexp = r'\[([0-9][+-]+|[0-9]|<)\]'
    code_digits = re.findall(regexp, code)

    results = []
    for index, digit in enumerate(code_digits):
        num = digit[0]
        match num:
            case '<':
                if index == 0:
                    return 'null'
                else: 
                    results.append(results[-1])
            case _:
                num = int(digit[0])
                ops = digit[1:len(digit)]

                for op in ops:
                    match op:
                        case '+':
                            num += 1
                        case '-':
                            num -= 1

                results.append(str(num  % 10))
    if len(results) < 4:
        return 'null'
    else:
        decrypted = ''.join(results)
        return decrypted
      
print(decode_santa_pin3('[1++][2-][3+][<]'))
print(decode_santa_pin3('[1++][][aaab][2-][4][<]9999+'))