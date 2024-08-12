# função que recebe uma lista de numeros e soma todos os elementos da lista

def somarTudo(lista):
    soma = 0
    soma = sum(lista)
    
    return soma

listaNumeros = [1,543, 2 ,11, 3, 443, 34]
resultado = somarTudo(listaNumeros)
print(resultado)