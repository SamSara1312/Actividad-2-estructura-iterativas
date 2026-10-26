"""Cuenta cuántos números son mayores, menores e iguales a 0."""
cantidad = int(input("¿Cuántos números vas a ingresar?: "))

mayores = 0
menores = 0
iguales = 0

for _ in range(cantidad):
    num = float(input("Ingresa un número: "))
    if num > 0:
        mayores += 1
    elif num < 0:
        menores += 1
    else:
        iguales += 1

print(f"Mayores que 0: {mayores}")
print(f"Menores que 0: {menores}")
print(f"Iguales a 0: {iguales}")