"""Indica si una letra es vocal o consonante, termina con espacio."""
VOCALES = "aeiouAEIOU"

while True:
    letra = input("Ingresa una letra (espacio para salir): ")
    if letra == " ":
        print("Programa terminado.")
        break
    if len(letra) != 1 or not letra.isalpha():
        print("Ingresa solo una letra.")
        continue
    if letra in VOCALES:
        print(f"{letra} es vocal.")
    else:
        print(f"{letra} es consonante.")