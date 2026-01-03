'''
Day 12: Enunciado
Dos elfos están jugando una batalla por turnos. Cada uno tiene un mazo
de movimientos que se representan como un string donde cada carácter es
una acción.

A Ataque normal: causa 1 punto de daño si no es bloqueado
B Bloqueo: bloquea un ataque normal (A)
F Ataque fuerte: causa 2 puntos de daño, no puede ser bloqueado
Ambos elfos comienzan con 3 puntos de vida. El primer elfo que llegue a
0 puntos de vida o menos pierde y la batalla termina inmediatamente (no
se siguen procesando más movimientos).

Reglas por ronda

Si ambos usan ataque (A o F), ambos reciben daño según el tipo.
B bloquea A, pero no bloquea F.
Todo se resuelve simultáneamente.
Tu tarea

Devuelve el resultado de la batalla como un número:

1 → si el Elfo 1 gana
2 → si el Elfo 2 gana
0 → si empatan (ambos llegan a 0 a la vez o terminan con la misma vida)
elfBattle('A', 'B')
// Ronda 1: A vs B -> Elfo 2 bloquea
// Resultado: Elfo 1 = 3 de vida
//            Elfo 2 = 3 de vida
// → 0

elfBattle('F', 'B')
// Ronda 1: F vs B -> Elfo 2 recibe 2 de daño (F no se bloquea)
// Resultado: Elfo 1 = 3 de vida
//            Elfo 2 = 1 de vida
// → 1

elfBattle('AAB', 'BBA')
// R1: A vs B → Elfo 2 bloquea
// R2: A vs B → Elfo 2 bloquea
// R3: B vs A → Elfo 1 bloquea
// Resultado: Elfo 1 = 3, Elfo 2 = 3
// → 0

elfBattle('AFA', 'BBA')
// R1: A vs B → Elfo 2 bloquea
// R2: F vs B → Elfo 2 recibe 2 de daño (F no se bloquea)
// R3: A vs A → ambos -1
// Resultado: Elfo 1 = 2, Elfo 2 = 0
// → 1

elfBattle('AFAB', 'BBAF')
// R1: A vs B → Elfo 2 bloquea
// R2: F vs B → Elfo 2 recibe 2 de daño (F no se bloquea)
// R3: A vs A → ambos -1 → Elfo 2 llega a 0 ¡Batalla termina!
// R4: no se juega, ya que Elfo 2 no tiene vida
// → 1

elfBattle('AA', 'FF')
// R1: A vs F → Elfo 1 -2, Elfo 2 -1
// R2: A vs F → Elfo 1 -2, Elfo 2 -1 → Elfo 1 llega a -1
// → 2
'''

#Versión de 3 estrellas
def elf_battle(elf1: str, elf2: str) -> int:
    elf1_life = 3
    elf2_life = 3
    rounds = len(elf1)

    for round in range(rounds):
        elf1_movement = elf1[round]
        elf2_movement = elf2[round]

        # F Movement
        if elf1_movement == 'F':
            elf2_life -= 2
            if elf2_movement == 'A':
                elf1_life -= 1
        if elf2_movement == 'F':
            elf1_life -= 2
            if elf1_movement == 'A':
                elf2_life -= 1
        
        # A Movement
        if elf1_movement == 'A' and elf2_movement == 'A':
            elf1_life -= 1
            elf2_life -= 1

        # print("Round(" + str(round + 1) + ") Elf1: " + str(elf1_life) + " Elf2: " + str(elf2_life))

        # Faster finish
        if elf1_life == elf2_life and elf1_life <= 0:
            return 0
        if elf1_life == 0 and elf2_life > 0:
            return 2
        if elf2_life == 0 and elf1_life > 0:
            return 1
    
    # Normal finish
    if elf1_life > elf2_life:
        return 1
    if elf2_life > elf1_life:
        return 2
    if elf1_life == elf2_life:
        return 0

winner = elf_battle('AAB', 'BAA')
# → 0
print(winner)

winner2 = elf_battle('AFA', 'BBA')
# → 1
print(winner2)

winner3 = elf_battle('AFAB', 'BBAF')
# → 1
print(winner3)

winner4 = elf_battle('AA', 'FF')
# → 2
print(winner4)

winner5 = elf_battle('AFAB', 'BBAF')
# → 1
print(winner5)

winner6 = elf_battle('AAFFFBBB', 'ABBBBFFF')
# → 1
print(winner6)
