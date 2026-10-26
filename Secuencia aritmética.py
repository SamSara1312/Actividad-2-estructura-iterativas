"""Genera una secuencia aritmética hasta un máximo con do-while simulado."""
inicio = int(input("Primer número: "))
diferencia = int(input("Diferencia: "))
maximo = int(input("Número máximo: "))

actual = inicio

while True:
    print(actual)
    if actual >= maximo:
        break
    actual += diferencia