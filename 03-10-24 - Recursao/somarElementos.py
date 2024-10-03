# somar elementos de uma lista e retorna

def somarElementos(lista):
    
    posicao = len(lista)
    
    if posicao == 0:
        return 0

    else:
        return lista[0] + somarElementos(lista[1:])


soma = somarElementos([1, 4, 2, 4, 5])
print(soma) 
