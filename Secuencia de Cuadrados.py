"""Muestra los cuadrados de 1 hasta N con do-while simulado."""
n = int(input("Ingresa un número entero positivo: "))
contador = 1

while True:
    print(f"{contador} al cuadrado es {contador ** 2}")
    if contador >= n:
        break
    contador += 1