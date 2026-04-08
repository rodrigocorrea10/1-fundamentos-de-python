def separar_pares_impares(lista):
    pares = [n for n in lista if n % 2 == 0]
    impares = [n for n in lista if n % 2 != 0]
    return pares, impares


def sistema():
    print("=== Separador de Números ===")
    
    entrada = input("Digite vários números separados por espaço: ")
    
    # transforma a entrada em lista de números
    numeros = [int(n) for n in entrada.split()]
    
    pares, impares = separar_pares_impares(numeros)
    
    print("\nResultado:")
    print("Pares:", pares)
    print("Ímpares:", impares)

