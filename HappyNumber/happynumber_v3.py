def es_numero_feliz_optimizado(numero, valor_final, potencia):
    tortuga = numero
    liebre = numero

    while True:
        tortuga = sum(int(digit) ** potencia for digit in str(tortuga))
        liebre = sum(int(digit) ** potencia for digit in str(liebre))
        liebre = sum(int(digit) ** potencia for digit in str(liebre))

        if tortuga == valor_final or liebre == valor_final:
            return True
        if tortuga == liebre:
            return False

def imprimir_happy_numbers_optimizado(cantidad, valor_final, potencia):
    happy_numbers = []
    numero = 1

    while len(happy_numbers) < cantidad:
        if es_numero_feliz_optimizado(numero, valor_final, potencia):
            happy_numbers.append(numero)
        numero += 1

    return happy_numbers

# Solicitar valores al usuario
try:
    print("#"*12+" Programa Numeros Felices Variante B "+"#"*12)
    X = int(input("Ingrese la cantidad de números felices que desea imprimir: "))
    valor_final = int(input("Ingrese el valor final al que hay que llegar (por ejemplo, 1 para los happy numbers): "))
    potencia = int(input("Ingrese la potencia aplicada (por ejemplo, 2 para los happy numbers): "))

    if X <= 0 or valor_final <= 0:
        print("Por favor, ingrese valores positivos mayores que cero.")
    else:
        # Imprimir los resultados utilizando la función optimizada
        happy_numbers = imprimir_happy_numbers_optimizado(X, valor_final, potencia)
        print(f"Los primeros {X} números felices son: {happy_numbers}")
except ValueError:
    print("Por favor, ingrese valores enteros válidos.")
