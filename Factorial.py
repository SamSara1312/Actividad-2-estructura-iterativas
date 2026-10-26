"""Calcula el factorial de un número usando for."""
numero = int(input("Ingresa un número: "))

factorial = 1
if numero < 0:
    print("No existe factorial de negativos.")
else:
    for i in range(1, numero + 1):
        factorial *= i
    print(f"El factorial de {numero} es: {factorial}")