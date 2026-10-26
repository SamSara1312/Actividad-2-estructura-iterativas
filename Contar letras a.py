"""Cuenta cuántas veces aparece la letra 'a' en una palabra."""
palabra = input("Ingresa una palabra: ").lower()

contador = 0
for letra in palabra:
    if letra == 'a':
        contador += 1

print(f"La letra 'a' aparece {contador} veces.")