"""Calcula la media de números positivos, termina con negativo."""
suma = 0
contador = 0

while True:
    numero = float(input("Ingresa un número positivo (negativo para terminar): "))
    if numero < 0:
        break
    suma += numero
    contador += 1

if contador > 0:
    media = suma / contador
    print(f"La media es: {media:.2f}")
else:
    print("No ingresaste números positivos.")