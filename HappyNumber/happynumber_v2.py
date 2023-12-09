def es_numero_feliz(numero, valor_final, potencia):
    historial = set()
    while numero != valor_final and numero not in historial:
        historial.add(numero)
        numero = sum(int(digit) ** potencia for digit in str(numero))
    return numero == valor_final

def imprimir_happy_numbers(cantidad, valor_final, potencia):
    happy_numbers = []
    numero = 1

    while len(happy_numbers) < cantidad:
        if es_numero_feliz(numero, valor_final, potencia):
            happy_numbers.append(numero)
        numero += 1

    return happy_numbers

# Solicitar valores al usuario
try:
    print("#"*12+" Programa Numeros Felices Variante A "+"#"*12)
    X = int(input("Ingrese la cantidad de números felices que desea imprimir: "))
    valor_final = int(input("Ingrese el valor final al que hay que llegar (por ejemplo, 1 para los happy numbers): "))
    potencia = int(input("Ingrese la potencia aplicada (por ejemplo, 2 para los happy numbers): "))

    if X <= 0 or valor_final <= 0:
        print("Por favor, ingrese valores positivos mayores que cero.")
    else:
        # Imprimir los resultados
        happy_numbers = imprimir_happy_numbers(X, valor_final, potencia)
        print(f"Los primeros {X} números felices son: {happy_numbers}")
except ValueError:
    print("Por favor, ingrese valores enteros válidos.")
