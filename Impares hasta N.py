"""Muestra números impares desde 1 hasta N con do-while simulado."""
n = int(input("Ingresa un número entero positivo: "))
contador = 1

while True:
    if contador % 2 != 0:
        print(contador)
    if contador >= n:
        break
    contador += 1