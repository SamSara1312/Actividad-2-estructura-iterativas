"""Juego para adivinar un número aleatorio del 1 al 100."""
import random

NUM_MIN = 1
NUM_MAX = 100

secreto = random.randint(NUM_MIN, NUM_MAX)
intento = 0

print(f"Adivina el número entre {NUM_MIN} y {NUM_MAX}")

while intento != secreto:
    intento = int(input("Tu intento: "))
    if intento < secreto:
        print("Demasiado bajo.")
    elif intento > secreto:
        print("Demasiado alto.")
    else:
        print(f"¡Correcto! El número era {secreto}")