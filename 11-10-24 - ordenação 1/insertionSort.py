def insertionSort(lista):
    n = len(lista)
    for i in range(1, n):
        marcado = lista[i]
        j = i - 1
        while j >= 0 and marcado < lista[j]:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = marcado
    
    return lista

listaOrdenada = insertionSort(['Gustavo', 'Calebe', 'Caetano', 'Artur', 'Vitorio', 'Lucas', 'Jhoni'])

print(listaOrdenada)