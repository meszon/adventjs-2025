'''
Day 5: Enunciado
Los elfos tienen un timestamp secreto: es la fecha y hora exacta en la que Papá Noel despega con
el trineo para repartir regalos por el mundo. Pero en el Polo Norte usan un formato rarísimo para
guardar la hora: YYYY*MM*DD@HH|mm|ss NP (ejemplo: 2025*12*25@00|00|00 NP).

Tu misión es escribir una función que reciba:

fromTime → fecha de referencia en formato elfo (YYYY*MM*DD@HH|mm|ss NP).
takeOffTime → la misma fecha de despegue, también en formato elfo.
La función debe devolver:

Los segundos completos que faltan para el despegue.
Si ya estamos en el despegue exacto → 0.
Si el despegue ya ocurrió → un número negativo indicando cuántos segundos han pasado desde entonces.

Reglas
Convierte el formato elfo a un timestamp primero. El sufijo NP indica la hora oficial del Polo Norte
(sin husos horarios ni DST), así que puedes tratarlo como si fuera UTC.
Usa diferencias en segundos, no en milisegundos.
Redondea siempre hacia abajo (floor): solo segundos completos.

Ejemplos
const takeoff = '2025*12*25@00|00|00 NP'

// desde el 24 diciembre 2025, 23:59:30, 30 segundos antes del despegue
timeUntilTakeOff('2025*12*24@23|59|30 NP', takeoff)
// 30

// justo en el momento exacto
timeUntilTakeOff('2025*12*25@00|00|00 NP', takeoff)
// 0

// 12 segundos después del despegue
timeUntilTakeOff('2025*12*25@00|00|12 NP', takeoff)
// -12
'''
from datetime import datetime

#Versión de 5 estrellas
def time_until_take_off(from_time: str, take_off_time: str) -> int:
  format = '%Y*%m*%d@%H|%M|%S NP'

  format_from_time = datetime.strptime(from_time, format)
  format_take_off_time =datetime.strptime(take_off_time, format)

  sub = format_take_off_time - format_from_time
  time_left = (sub.days * 86400) + sub.seconds + (sub.microseconds / 10**6)
  
  return (int(time_left))

takeoff = '2025*12*25@00|00|00 NP'
result = time_until_take_off('2025*12*24@23|59|30 NP', takeoff)
print(result)