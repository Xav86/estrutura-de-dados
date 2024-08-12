# criar uma Função que recebe uma lista fazia e permite adicionar 5 elementos nela, ao final exibir essa lista ao usuário

def retornaLista(lista):
    itens = 1
    listaNova = []
    while itens < 6:
        item = input(f"Digite o item {itens} da lista: ")
        listaNova.append(item)
        
        itens += 1
        
    return listaNova

listaVazia = [] # o que sera que tem dentro dessa lista?
listaNaoVazia = retornaLista(listaVazia)
print(listaNaoVazia)