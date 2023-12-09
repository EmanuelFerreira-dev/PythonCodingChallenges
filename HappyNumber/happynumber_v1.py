def es_numero_feliz(numero):
    historial = set()
    while numero != 1 and numero not in historial:
        historial.add(numero)
        numero = sum(int(digit) ** 2 for digit in str(numero))
    return numero == 1

def imprimir_happy_numbers(cantidad):
    happy_numbers = []
    numero = 1

    while len(happy_numbers) < cantidad:
        if es_numero_feliz(numero):
            happy_numbers.append(numero)
        numero += 1

    return happy_numbers

# Solicitar la cantidad de números felices al usuario
while True:
    try:
        print("#"*12+" Programa Numeros Felices "+"#"*12)
        X = int(input("Ingrese la cantidad de números felices que desea imprimir: "))
        print("#"*30)
        if X <= 0:
            print("Por favor, ingrese un número positivo mayor que cero.")
        else:
            # Imprimir los resultados
            happy_numbers = imprimir_happy_numbers(X)
            print(f"Los primeros {X} números felices son: {happy_numbers}")
            break  # Salir del bucle si la entrada es válida
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
