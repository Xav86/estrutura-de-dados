# função que recebe uma lista de numeros inteiros e retorna uma nova lista

def listaNumero(list):
    i = 0
    listPar = []
    for i in list:
        if list[i] % 2 == 0:
            listPar.insert(list[i])

list = [1,2,3,4,5,6,7,8,9,10]

result = listaNumero(list)

print(result)