"""Calculadora básica que pregunta si desea continuar."""
while True:
    print("\n1. Suma 2. Resta 3. Multiplicación 4. División")
    opcion = input("Elige operación (1-4): ")
    
    num1 = float(input("Primer número: "))
    num2 = float(input("Segundo número: "))

    match opcion:
        case "1":
            print(f"Resultado: {num1 + num2}")
        case "2":
            print(f"Resultado: {num1 - num2}")
        case "3":
            print(f"Resultado: {num1 * num2}")
        case "4":
            if num2 != 0:
                print(f"Resultado: {num1 / num2}")
            else:
                print("No se puede dividir entre cero.")
        case _:
            print("Opción no válida.")

    continuar = input("¿Deseas continuar? (s/n): ").lower()
    if continuar != 's':
        break