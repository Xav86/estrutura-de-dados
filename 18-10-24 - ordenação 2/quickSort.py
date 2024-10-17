
def particao(lista, inicio, final):
    pivo = lista[final]
    i = inicio -1

    for j in range(inicio, final):
        if lista[j] <= pivo:
            i = i + 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i + 1], lista[final] = lista[final], lista[i + 1]

    return i + 1

def quickSort(lista, inicio, final):
    if inicio < final:
        posicao = particao(lista, inicio, final)

        #esquerda
        quickSort(lista, inicio, posicao -1)

        #direita
        quickSort(lista, posicao +1, final)
    
    return lista
