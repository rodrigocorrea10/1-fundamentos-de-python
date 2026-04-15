def boring_function(parametro):
    print('Recebi o parametro', parametro)
    soma = parametro
    for i in range (3):
        soma += 1
    return soma

var = int(input('Digite um valor: '))
x = boring_function(var)
print("O resultado da função é:", x)
 
