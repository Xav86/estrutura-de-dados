# função que recebe uma lista de numeros inteiros e retorna uma nova lista

def lista_numero(lista):
    lista_par = []
    for i in lista:
        if i % 2 == 0:
            lista_par.append(i)
    return lista_par

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

result = lista_numero(lista)

print(result)