"""Determina cuántos dígitos tiene un número entero."""
numero = input("Ingresa un número entero: ")

# Quitamos signo negativo si existe
numero_limpio = numero.lstrip('-')
print(f"El número tiene {len(numero_limpio)} dígitos.")