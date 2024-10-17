
def mergeSort(lista):
    #divisão do array
    if len(lista) > 1:
        divisao = lista[:len(lista)//2]

        esquerda = lista[:divisao]
        direita = lista[divisao:]

        mergeSort(esquerda)
        mergeSort(direita)

        i, j, k = 0

    # Ordena esquerda e direita
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            lista[k] = esquerda[i]
            i += 1
        else:
            lista[k] = direita[j]
            j += 1
        
        k += 1

    # Ordenação final
    while i < len(esquerda):
        lista[k] = esquerda[i]
        i += 1
        k += 1

    while j < len(direita):
        lista[k] = direita[j]
        j += 1
        k += 1

    return lista